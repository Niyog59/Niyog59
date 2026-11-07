<p align="center">
  <img src="assets/banner.svg" alt="Niyog Uprety. Data Engineer, Data Analyst, Python and SQL. I like building things." width="100%">
</p>

**Houston based · Data Engineer / Data Analyst · Graduating May 2027 · Open to full time data roles**

<a href="https://www.linkedin.com/in/niyog-uprety-177b9621a/"><img src="assets/linkedin.svg" alt="Connect on LinkedIn" height="36"></a> <a href="https://jobobservatory.dev"><img src="assets/projects/job-observatory-stats.svg" alt="Job Observatory live stats" height="36"></a>

Hi, I'm Niyog. I like building data pipelines and then poking at the data they collect. Most
of my work is Python and SQL: getting data in reliably, keeping it honest, and turning it into
something I can actually answer questions with.

<!-- OBSERVATORY_STATS:START -->
51 employer boards checked three times a day · 148 open jobs tracked right now · 259 jobs kept in total · requirements extracted on 166 of 167 kept postings (99%) · updated 2026-11-05
<!-- OBSERVATORY_STATS:END -->

## Job Observatory

<a href="https://github.com/Niyog59/Job-Market-Intelligence"><img src="assets/projects/job-observatory-logo.png" alt="Job Observatory logo" width="84"></a>

- **What it is:** a pipeline and website that collects job listings from employer boards and keeps every version of every listing, live on one AWS server since November 4, 2026.
- **The hard part:** an AI model pulls requirements out of each listing, and Python checks every answer against the listing text before dbt turns the history into reports. Only complete scans count as proof a job closed.

I host it on AWS, on one EC2 server. Python collectors pull the postings from <!--PROFILE:boards-->51<!--/PROFILE:boards--> Greenhouse and Lever boards, three times a day, and the jobs show up on the live site for anyone to search. Airflow runs the whole schedule: collection, extraction, the dbt build, and publishing, and it retries anything that failed every 15 minutes. Raw pages go to S3 as they are collected, and the database is backed up to S3, so the data is not only on the server.

An AI model reads each posting and pulls out the requirements, the location, and the job family into fixed fields. Every value it returns has to quote the posting it came from, word for word. dbt turns those fields into the reporting tables. The reports page and the dashboard feed are rebuilt from those tables at every publish, so the dashboards always run on the newest batch of data.

I also tested Spark. I rebuilt three of the reporting models in PySpark and ran them on Databricks, to see whether Spark would do that step better than PostgreSQL. It did not. The data is small enough to fit in one database, so Spark's overhead cost more than the parallel work saved, and the live system stayed on PostgreSQL. The Spark code and the timings are in the repo. Spark and Databricks are not part of the running system.

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/postgresql-dark.svg"><img src="assets/stack/postgresql-light.svg" alt="PostgreSQL" title="PostgreSQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/dbt-dark.svg"><img src="assets/stack/dbt-light.svg" alt="dbt" title="dbt" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/airflow-dark.svg"><img src="assets/stack/airflow-light.svg" alt="Airflow" title="Airflow" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/aws-dark.svg"><img src="assets/stack/aws-light.svg" alt="AWS" title="AWS" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/docker-dark.svg"><img src="assets/stack/docker-light.svg" alt="Docker" title="Docker" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/databricks-dark.svg"><img src="assets/stack/databricks-light.svg" alt="Databricks" title="Databricks" height="24"></picture>
</p>

[Live site](https://jobobservatory.dev) · [Reports](https://jobobservatory.dev/reports) · [Source](https://github.com/Niyog59/Job-Market-Intelligence) · [What went wrong](https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md) · [Spark and Databricks comparison](https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/spark/README.md)

### What the job data shows

<!-- OBSERVATORY_INSIGHTS:START -->
Of the 148 open data, analytics, and software jobs I track in Dallas-Fort Worth, Houston, and remote-for-Texas (29 employers, collected through 2026-11-05), only 10% of those with a clear level are junior and 84% are senior or above. 27% mention generative AI. It is a small group of employers and a single snapshot, so it describes these listings, not the whole market.
<!-- OBSERVATORY_INSIGHTS:END -->

## Other projects

<a href="https://github.com/Niyog59/TalentYak"><img src="assets/products/talentyak.png" alt="TalentYak logo" width="72"></a>

### [TalentYak](https://github.com/Niyog59/TalentYak)

I built TalentYak for Nepali fitness coaches and Nepalis living abroad. Coaches get a profile, sell packages, message clients, and track their progress in one place. The parts I spent the most time on were not the visible ones: row-level security so people only see their own records, money kept as integers so amounts never round wrong, and Stripe events that can arrive twice without doing anything twice. The site is live in test mode, so no real payments yet.

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/nextjs-dark.svg"><img src="assets/stack/nextjs-light.svg" alt="Next.js" title="Next.js" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/typescript-dark.svg"><img src="assets/stack/typescript-light.svg" alt="TypeScript" title="TypeScript" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/react-dark.svg"><img src="assets/stack/react-light.svg" alt="React" title="React" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/supabase-dark.svg"><img src="assets/stack/supabase-light.svg" alt="Supabase" title="Supabase" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/vercel-dark.svg"><img src="assets/stack/vercel-light.svg" alt="Vercel" title="Vercel" height="24"></picture>
</p>

<p><a href="https://talentyak.com">Live site</a> · <a href="https://github.com/Niyog59/TalentYak">Source</a> · <a href="https://github.com/Niyog59/TalentYak/blob/main/docs/PORTFOLIO.md">Technical overview</a></p>

<a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI"><img src="assets/projects/vendor-performance-logo.png" alt="Vendor Performance Analysis logo" width="72"></a>

### [Vendor Performance Analysis](https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI)

A liquor distributor's purchase and sales records, in SQLite, SQL, Python, and Power BI. I wanted to see where the money actually goes. The top 10 vendors take about 66% of purchase dollars, and about $2.71M is tied up in inventory that has not sold. The written report and the dashboard are in the repo.

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/sql-dark.svg"><img src="assets/stack/sql-light.svg" alt="SQL" title="SQL" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/python-dark.svg"><img src="assets/stack/python-light.svg" alt="Python" title="Python" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/pandas-dark.svg"><img src="assets/stack/pandas-light.svg" alt="pandas" title="pandas" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/powerbi-dark.svg"><img src="assets/stack/powerbi-light.svg" alt="Power BI" title="Power BI" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/jupyter-dark.svg"><img src="assets/stack/jupyter-light.svg" alt="Jupyter" title="Jupyter" height="24"></picture>
</p>

<p><a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI">Source</a> · <a href="https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI/blob/main/Vendor%20Performance%20Report.pdf">Report (PDF)</a></p>

<a href="https://github.com/Niyog59/Airline-Profitability"><img src="assets/projects/airline-profitability-logo.png" alt="Airline Route Profitability logo" width="72"></a>

### [Airline Route Profitability](https://github.com/Niyog59/Airline-Profitability)

Built with Shaheer Ahmed. We looked at 7,974 simulated flights for a Dubai-based airline, and at which routes make money. Long-haul flights averaged about $160K profit per flight. Short-haul flights lost about $9K on average. The data is simulated, so these are patterns in the dataset, not causes.

<p>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/r-dark.svg"><img src="assets/stack/r-light.svg" alt="R" title="R" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/tidyverse-dark.svg"><img src="assets/stack/tidyverse-light.svg" alt="tidyverse" title="tidyverse" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/ggplot2-dark.svg"><img src="assets/stack/ggplot2-light.svg" alt="ggplot2" title="ggplot2" height="24"></picture>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/stack/rstudio-dark.svg"><img src="assets/stack/rstudio-light.svg" alt="RStudio" title="RStudio" height="24"></picture>
</p>

<p><a href="https://github.com/Niyog59/Airline-Profitability">Source</a></p>

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
