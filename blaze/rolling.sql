with subset as (
  select * from nyc limit 10000000
), computed as (
  select
    date_trunc('day', pickup_datetime) as ts,
    avg(mta_tax) as avg_mta_tax
  from
    subset
  group by
    ts
), dates as (
  select generate_series(
    (select min(ts) from computed),
    (select max(ts) from computed),
    interval '1 day'
  ) as ts
), result as (
  select
    dates.ts,
    computed.avg_mta_tax
  from
    dates
      left outer join
    computed
      using (ts)
  order by
    dates.ts
)
select
  r.ts,
  r.mta_tax,
  avg(r.mta_tax) over w as rolling_avg_mta_tax,
  stdev(r.mta_tax) over w as rolling_std_mta_tax
from subset as r
window w as (order by ts rows between 6 preceding and current row);
