<p align="center">
  <img src="assets/banner.svg" alt="Niyog Uprety. Data Engineer, Data Analyst, Python and SQL. I like building things." width="100%">
</p>

**Houston based · Data Engineer / Data Analyst · Graduating May 2027 · Open to full time data roles**

<a href="https://www.linkedin.com/in/niyog-uprety-177b9621a/"><img src="assets/linkedin.svg" alt="Connect on LinkedIn" height="36"></a> <a href="https://jobobservatory.dev"><img src="assets/projects/job-observatory-stats.svg" alt="Job Observatory live stats" height="36"></a>

Hi, I'm Niyog. I build data pipelines in Python and SQL, keep the data they collect honest, and turn it into answers. The first project below is a job market pipeline that runs twice a day on its own server.

<!-- OBSERVATORY_STATS:START -->
51 employer boards checked twice a day · 148 open jobs tracked right now · 259 jobs kept in total · requirements extracted on 166 of 167 kept postings (99%) · updated 2026-11-05
<!-- OBSERVATORY_STATS:END -->

## Job Observatory

<a href="https://github.com/Niyog59/Job-Market-Intelligence"><img src="assets/projects/job-observatory-logo.png" alt="Job Observatory logo" width="84"></a>

- **What it is:** a pipeline and website that collects job listings from employer boards and keeps every version of every listing, live on one AWS server since November 4, 2026.
- **The hard part:** an AI model pulls requirements out of each listing, and Python checks every answer against the listing text before dbt turns the history into reports. Only complete scans count as proof a job closed.
- **Measured:** collecting all boards takes 133 seconds; 46 dbt models and 125 data tests pass in CI; a Spark vs PostgreSQL test on 6.6M rows kept PostgreSQL (5.18s vs 12.40s, identical results).

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="24"></picture>
</p>

[Live site](https://jobobservatory.dev) · [Reports](https://jobobservatory.dev/reports) · [Source](https://github.com/Niyog59/Job-Market-Intelligence) · [What went wrong](https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md)

### What the job data shows

<!-- OBSERVATORY_INSIGHTS:START -->
Of the 148 open data, analytics, and software jobs I track in Dallas-Fort Worth, Houston, and remote-for-Texas (29 employers, collected through 2026-11-05), only 10% of those with a clear level are junior and 84% are senior or above. 27% mention generative AI. It is a small group of employers and a single snapshot, so it describes these listings, not the whole market.
<!-- OBSERVATORY_INSIGHTS:END -->

## Other projects

<table>
<tr>
<td width="33%" valign="top">
<a href="https://github.com/Niyog59/TalentYak"><img src="assets/products/talentyak.png" alt="TalentYak logo" width="72"></a>
<h3><a href="https://github.com/Niyog59/TalentYak">TalentYak</a></h3>
<ul>
<li><b>What:</b> fitness coaching platform for Nepali coaches and clients abroad, designed and built on my own.</li>
<li><b>Hard part:</b> PostgreSQL row-level security, money stored as integers with tests, Stripe events safe to receive twice.</li>
<li><b>Status:</b> test site live; no real payments.</li>
</ul>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="24"></picture>
</p>
<p><a href="https://jobobservatory.dev">Live site</a> · <a href="https://jobobservatory.dev/reports">Reports</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence">Source</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md">What went wrong</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/TalentYak"><img src="assets/products/talentyak.png" alt="TalentYak logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/TalentYak">TalentYak</a></h3>
<p>A fitness coaching platform for Nepali coaches and clients abroad, designed and built on my own. The interesting work is in the data layer: PostgreSQL row-level security so people only see their own records, money stored as integers with tests, and Stripe payment events that are safe to receive twice. The test site is live; it handles no real payments.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/nextjs-dark.svg"><img src="assets/stack/nextjs-light.svg" alt="Next.js" title="Next.js" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/typescript-dark.svg"><img src="assets/stack/typescript-light.svg" alt="TypeScript" title="TypeScript" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/react-dark.svg"><img src="assets/stack/react-light.svg" alt="React" title="React" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/supabase-dark.svg"><img src="assets/stack/supabase-light.svg" alt="Supabase" title="Supabase" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/vercel-dark.svg"><img src="assets/stack/vercel-light.svg" alt="Vercel" title="Vercel" height="24"></picture>
</p>
<p><a href="https://talentyak.com">Live site</a> · <a href="https://github.com/Niyog59/TalentYak">Source</a> · <a href="https://github.com/Niyog59/TalentYak/blob/main/docs/PORTFOLIO.md">Technical overview</a></p>
</td>
<td width="33%" valign="top">
<a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI"><img src="assets/projects/vendor-performance-logo.png" alt="Vendor Performance Analysis logo" width="72"></a>
<h3><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Vendor Performance Analysis</a></h3>
<ul>
<li><b>What:</b> a liquor distributor's purchases and sales, loaded into SQLite, summarized in SQL, analyzed in Python and Power BI.</li>
<li><b>Finding:</b> top 10 vendors are about 66% of purchase dollars; about $2.71M tied up in unsold inventory.</li>
<li><b>In the repo:</b> written report and Power BI dashboard.</li>
</ul>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="24"></picture>
</p>
<p><a href="https://jobobservatory.dev">Live site</a> · <a href="https://jobobservatory.dev/reports">Reports</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence">Source</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md">What went wrong</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/TalentYak"><img src="assets/products/talentyak.png" alt="TalentYak logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/TalentYak">TalentYak</a></h3>
<p>A fitness coaching platform for Nepali coaches and clients abroad, designed and built on my own. The interesting work is in the data layer: PostgreSQL row-level security so people only see their own records, money stored as integers with tests, and Stripe payment events that are safe to receive twice. The test site is live; it handles no real payments.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/nextjs-dark.svg"><img src="assets/stack/nextjs-light.svg" alt="Next.js" title="Next.js" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/typescript-dark.svg"><img src="assets/stack/typescript-light.svg" alt="TypeScript" title="TypeScript" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/react-dark.svg"><img src="assets/stack/react-light.svg" alt="React" title="React" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/supabase-dark.svg"><img src="assets/stack/supabase-light.svg" alt="Supabase" title="Supabase" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/vercel-dark.svg"><img src="assets/stack/vercel-light.svg" alt="Vercel" title="Vercel" height="24"></picture>
</p>
<p><a href="https://talentyak.com">Live site</a> · <a href="https://github.com/Niyog59/TalentYak">Source</a> · <a href="https://github.com/Niyog59/TalentYak/blob/main/docs/PORTFOLIO.md">Technical overview</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI"><img src="assets/projects/vendor-performance-logo.png" alt="Vendor Performance Analysis logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Vendor Performance Analysis</a></h3>
<p>A liquor distributor's purchase and sales records, loaded into SQLite, summarized in SQL, and analyzed in Python and Power BI. The top 10 vendors account for about 66% of purchase dollars, and about $2.71M is tied up in unsold inventory. The repo includes the written report and the Power BI dashboard.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/sql-dark.svg"><img src="assets/stack/sql-light.svg" alt="SQL" title="SQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/pandas-dark.svg"><img src="assets/stack/pandas-light.svg" alt="pandas" title="pandas" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/powerbi-dark.svg"><img src="assets/stack/powerbi-light.svg" alt="Power BI" title="Power BI" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/jupyter-dark.svg"><img src="assets/stack/jupyter-light.svg" alt="Jupyter" title="Jupyter" height="24"></picture>
</p>
<p><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Source</a> · <a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI/blob/main/Vendor%20Performance%20Report.pdf">Report (PDF)</a></p>
</td>
<td width="33%" valign="top">
<a href="https://github.com/Niyog59/Airline-Profitability"><img src="assets/projects/airline-profitability-logo.png" alt="Airline Route Profitability logo" width="72"></a>
<h3><a href="https://github.com/Niyog59/Airline-Profitability">Airline Route Profitability</a></h3>
<ul>
<li><b>What:</b> R analysis of profitability across 7,974 simulated flights, built with Shaheer Ahmed.</li>
<li><b>Finding:</b> long-haul averaged about $160K profit per flight; short-haul lost about $9K on average.</li>
<li><b>Honest note:</b> simulated data, so these are patterns, not causes.</li>
</ul>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="24"></picture>
</p>
<p><a href="https://jobobservatory.dev">Live site</a> · <a href="https://jobobservatory.dev/reports">Reports</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence">Source</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md">What went wrong</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/TalentYak"><img src="assets/products/talentyak.png" alt="TalentYak logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/TalentYak">TalentYak</a></h3>
<p>A fitness coaching platform for Nepali coaches and clients abroad, designed and built on my own. The interesting work is in the data layer: PostgreSQL row-level security so people only see their own records, money stored as integers with tests, and Stripe payment events that are safe to receive twice. The test site is live; it handles no real payments.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/nextjs-dark.svg"><img src="assets/stack/nextjs-light.svg" alt="Next.js" title="Next.js" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/typescript-dark.svg"><img src="assets/stack/typescript-light.svg" alt="TypeScript" title="TypeScript" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/react-dark.svg"><img src="assets/stack/react-light.svg" alt="React" title="React" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/supabase-dark.svg"><img src="assets/stack/supabase-light.svg" alt="Supabase" title="Supabase" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/vercel-dark.svg"><img src="assets/stack/vercel-light.svg" alt="Vercel" title="Vercel" height="24"></picture>
</p>
<p><a href="https://talentyak.com">Live site</a> · <a href="https://github.com/Niyog59/TalentYak">Source</a> · <a href="https://github.com/Niyog59/TalentYak/blob/main/docs/PORTFOLIO.md">Technical overview</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI"><img src="assets/projects/vendor-performance-logo.png" alt="Vendor Performance Analysis logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Vendor Performance Analysis</a></h3>
<p>A liquor distributor's purchase and sales records, loaded into SQLite, summarized in SQL, and analyzed in Python and Power BI. The top 10 vendors account for about 66% of purchase dollars, and about $2.71M is tied up in unsold inventory. The repo includes the written report and the Power BI dashboard.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/sql-dark.svg"><img src="assets/stack/sql-light.svg" alt="SQL" title="SQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/pandas-dark.svg"><img src="assets/stack/pandas-light.svg" alt="pandas" title="pandas" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/powerbi-dark.svg"><img src="assets/stack/powerbi-light.svg" alt="Power BI" title="Power BI" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/jupyter-dark.svg"><img src="assets/stack/jupyter-light.svg" alt="Jupyter" title="Jupyter" height="24"></picture>
</p>
<p><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Source</a> · <a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI/blob/main/Vendor%20Performance%20Report.pdf">Report (PDF)</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/Niyog59/Airline-Profitability"><img src="assets/projects/airline-profitability-logo.png" alt="Airline Route Profitability logo" width="84"></a>
<h3><a href="https://github.com/Niyog59/Airline-Profitability">Airline Route Profitability</a></h3>
<p>Built with Shaheer Ahmed. An R analysis of profitability across 7,974 simulated flights for a Dubai-based airline (a Kaggle dataset). Long-haul flights averaged about $160K profit per flight, while short-haul flights lost about $9K on average. The data is simulated, so these are patterns in the dataset, not causes.</p>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/r-dark.svg"><img src="assets/stack/r-light.svg" alt="R" title="R" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/tidyverse-dark.svg"><img src="assets/stack/tidyverse-light.svg" alt="tidyverse" title="tidyverse" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/ggplot2-dark.svg"><img src="assets/stack/ggplot2-light.svg" alt="ggplot2" title="ggplot2" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/rstudio-dark.svg"><img src="assets/stack/rstudio-light.svg" alt="RStudio" title="RStudio" height="24"></picture>
</p>
<p><a href="https://github.com/Niyog59/Airline-Profitability">Source</a></p>
</td>
</tr>
</table>

## More projects

- [Airline occupancy in SQL and Python](https://github.com/Niyog59/Airlines-Data-Analysis-SQL-Python)
- [Gym database design in MySQL](https://github.com/Niyog59/Gym-Management-Project-MySQL)
- [Geocoding API with FastAPI](https://github.com/Niyog59/Geocoding-API)
- [MeetMerchants](https://meetmerchants.com), a B2B marketplace for businesses and suppliers in Nepal

## Tools

<p><b>Data</b><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/sql-dark.svg"><img src="assets/stack/sql-light.svg" alt="SQL" title="SQL" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/pandas-dark.svg"><img src="assets/stack/pandas-light.svg" alt="pandas" title="pandas" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/r-dark.svg"><img src="assets/stack/r-light.svg" alt="R" title="R" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/tidyverse-dark.svg"><img src="assets/stack/tidyverse-light.svg" alt="tidyverse" title="tidyverse" height="34"></picture>
</p>

<p><b>Reporting</b><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/tableau-dark.svg"><img src="assets/stack/tableau-light.svg" alt="Tableau" title="Tableau" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/powerbi-dark.svg"><img src="assets/stack/powerbi-light.svg" alt="Power BI" title="Power BI" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/ggplot2-dark.svg"><img src="assets/stack/ggplot2-light.svg" alt="ggplot2" title="ggplot2" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/jupyter-dark.svg"><img src="assets/stack/jupyter-light.svg" alt="Jupyter" title="Jupyter" height="34"></picture>
</p>

<p><b>Infrastructure</b><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/github-actions-dark.svg"><img src="assets/stack/github-actions-light.svg" alt="GitHub Actions" title="GitHub Actions" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/git-dark.svg"><img src="assets/stack/git-light.svg" alt="Git" title="Git" height="34"></picture>
</p>

<details>
<summary>Other tools I have used</summary>
<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/typescript-dark.svg"><img src="assets/stack/typescript-light.svg" alt="TypeScript" title="TypeScript" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/javascript-dark.svg"><img src="assets/stack/javascript-light.svg" alt="JavaScript" title="JavaScript" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/nextjs-dark.svg"><img src="assets/stack/nextjs-light.svg" alt="Next.js" title="Next.js" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/react-dark.svg"><img src="assets/stack/react-light.svg" alt="React" title="React" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/tailwindcss-dark.svg"><img src="assets/stack/tailwindcss-light.svg" alt="Tailwind CSS" title="Tailwind CSS" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/fastapi-dark.svg"><img src="assets/stack/fastapi-light.svg" alt="FastAPI" title="FastAPI" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/rest-apis-dark.svg"><img src="assets/stack/rest-apis-light.svg" alt="REST APIs" title="REST APIs" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/supabase-dark.svg"><img src="assets/stack/supabase-light.svg" alt="Supabase" title="Supabase" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/vercel-dark.svg"><img src="assets/stack/vercel-light.svg" alt="Vercel" title="Vercel" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/cloudflare-dark.svg"><img src="assets/stack/cloudflare-light.svg" alt="Cloudflare" title="Cloudflare" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/mysql-dark.svg"><img src="assets/stack/mysql-light.svg" alt="MySQL" title="MySQL" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/mysql-workbench-dark.svg"><img src="assets/stack/mysql-workbench-light.svg" alt="MySQL Workbench" title="MySQL Workbench" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/numpy-dark.svg"><img src="assets/stack/numpy-light.svg" alt="NumPy" title="NumPy" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/rstudio-dark.svg"><img src="assets/stack/rstudio-light.svg" alt="RStudio" title="RStudio" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/github-dark.svg"><img src="assets/stack/github-light.svg" alt="GitHub" title="GitHub" height="34"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/cursor-dark.svg"><img src="assets/stack/cursor-light.svg" alt="Cursor" title="Cursor" height="34"></picture>
</p>
</details>

## Contact

<a href="https://www.linkedin.com/in/niyog-uprety-177b9621a/">LinkedIn</a> · <a href="https://jobobservatory.dev">jobobservatory.dev</a>
