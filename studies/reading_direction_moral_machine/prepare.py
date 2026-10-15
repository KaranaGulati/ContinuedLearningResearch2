"""Build one row per decision from the Moral Machine first-session file.

Usage: python prepare.py <path to first.parquet> <output scenario parquet>
first.parquet is SharedResponsesFullFirstSessions.csv (OSF 3hvt2) reduced to the needed columns.
"""
import sys
import duckdb

ARABIC = ["DZA", "BHR", "EGY", "IRQ", "JOR", "KWT", "LBN", "LBY", "MRT", "MAR",
          "OMN", "PSE", "QAT", "SAU", "SDN", "SYR", "TUN", "ARE", "YEM"]
RTL_OTHER = ["ISR", "IRN", "AFG", "PAK"]
EXCLUDED = ["COM", "DJI", "SOM", "ERI", "TCD"]

src, out = sys.argv[1], sys.argv[2]
q = lambda xs: ", ".join(f"'{x}'" for x in xs)
con = duckdb.connect()
con.sql(f"""
COPY (
  WITH s AS (
    SELECT ResponseID,
           any_value(UserID) AS UserID,
           any_value(UserCountry3) AS country,
           any_value(Template) AS template,
           any_value(ScenarioOrder) AS scenario_order,
           any_value(ScenarioType) AS scenario_type,
           max(DescriptionShown) AS description_shown,
           count(*) AS n_rows,
           sum(LeftHand) AS n_left,
           sum(Saved) AS n_saved,
           -- the clicked outcome is the row with Saved = 0 (README: Saved is reverse-coded from the click)
           max(CASE WHEN LeftHand = 1 THEN 1 - Saved END) AS clicked_left,
           -- the stay (omission) outcome is the row with Intervention = 0
           max(CASE WHEN LeftHand = 1 THEN 1 - Intervention END) AS stay_on_left,
           max(CASE WHEN Intervention = 0 THEN 1 - Saved END) AS clicked_stay
    FROM read_parquet('{src}')
    GROUP BY ResponseID
  )
  SELECT *,
    CASE WHEN country IN ({q(ARABIC)}) THEN 'ARABIC'
         WHEN country IN ({q(RTL_OTHER)}) THEN 'RTL_OTHER'
         WHEN country IN ({q(EXCLUDED)}) OR country IS NULL OR country IN ('', 'NA', 'nan', 'NaN') THEN 'EXCLUDED'
         ELSE 'LTR' END AS grp
  FROM s
  WHERE n_rows = 2 AND n_left = 1 AND n_saved = 1
) TO '{out}' (FORMAT parquet)
""")
print(con.sql(f"""SELECT template, grp, count(*) AS decisions, count(DISTINCT UserID) AS users
                 FROM read_parquet('{out}') GROUP BY ALL ORDER BY template, grp"""))
