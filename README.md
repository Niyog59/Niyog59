<p align="center">
  <img src="assets/banner.svg" alt="Niyog Uprety. Data Engineer, Data Analyst, Python and SQL. I like building things." width="100%">
</p>

Hi, I'm Niyog. I like building data pipelines and then poking at the data they collect. Most
of my work is Python and SQL: getting data in reliably, keeping it honest, and turning it into
something I can actually answer questions with.

<a href="https://www.linkedin.com/in/niyog-uprety-177b9621a/"><img src="assets/linkedin.svg" alt="Connect on LinkedIn" height="36"></a>

## Job Observatory

<a href="https://jobobservatory.dev"><img src="assets/projects/job-observatory.png" alt="A job page on jobobservatory.dev: the job overview on the left and the requirements extracted from the description on the right, each with a link to the sentence it came from." width="100%"></a>

I wanted an easier way to find jobs without checking every company's career page, so I built
a pipeline that does it for me. Twice a day it collects listings from 51 employers' job boards, keeps every version
of every listing, and uses an AI model to pull out the requirements. Python checks each answer
and looks for every quoted line in the listing. dbt turns the history into tested tables, and
Airflow runs it all in Docker on one AWS server.

- Collecting all 51 boards took 133 seconds, and publishing the reports took 25 (measured on
  my Mac with the real data, 2026-11-03).
- I tested whether Spark would beat PostgreSQL for the reporting step. On 6.6 million rows of
  synthetic test data, PostgreSQL took 5.18 seconds and Spark 12.40 for the same three
  transformations, with identical results. I kept PostgreSQL.
- It runs in production at jobobservatory.dev since 2026-11-04, with nightly backups to S3.

<a href="https://jobobservatory.dev">Live site</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence">Source and write-up</a> · <a href="https://github.com/Niyog59/Job-Market-Intelligence/blob/main/docs/PROBLEMS.md">What went wrong</a>

## Analysis

**What the job data shows so far.** The pipeline publishes its own reports, and these are the
numbers I find most interesting.

<a href="https://jobobservatory.dev/insights"><img src="assets/projects/job-observatory-insights.png" alt="Market insights page: 148 open jobs, 29 employers, 10% junior and 84% senior or above among jobs with a clear level, 27% mention generative AI." width="100%"></a>

Of the 148 open data, analytics, and software jobs I track in Dallas-Fort Worth, Houston, and
remote-for-Texas (29 employers, collected through 2026-11-05), only 10% of those with a clear
level are junior. Among the 166 postings with extracted details, 38% list 5 to 7 years as
their minimum experience and only 13% ask for 2 years or less. It is a small group of employers and a single
snapshot, so it describes these listings, not the whole market.
<a href="https://jobobservatory.dev/reports">See the reports</a>

**[Airline Route Profitability](https://github.com/Niyog59/Airline-Profitability)**, with
Shaheer Ahmed. We used R to look at what goes with profit in a simulated year of 7,974 flights
for a Dubai-based airline (a Kaggle dataset). Long-haul flights averaged about $160K profit per
flight, while short-haul flights lost about $9K on average, and a third of all flights lost
money. Season and demand level lined up with profit too. Because the data is simulated and the
comparisons are by group, these are patterns in this dataset, not causes.
<sub>R · tidyverse · ggplot2 · R Markdown</sub>

**[Vendor Performance](https://github.com/Niyog59/Vendor-Performance-Analysis-SQL-Python-PowerBI)**.
I loaded a liquor distributor's purchase and sales records (a portfolio dataset) into SQLite,
built a vendor and brand summary in SQL, and analyzed it in Python and Power BI. The top 10
vendors made up about 66% of purchase dollars. Items bought in the largest quantities had about
72% lower unit costs than those bought in the smallest. That compares different products, so
it does not show that ordering more lowers the price.
<sub>SQL · SQLite · Python · pandas · Power BI</sub>

<sub>Also: [airline occupancy in SQL and Python](https://github.com/Niyog59/Airlines-Data-Analysis-SQL-Python) · [gym database design in MySQL](https://github.com/Niyog59/Gym-Management-Project-MySQL) · [geocoding API with FastAPI](https://github.com/Niyog59/Geocoding-API)</sub>

## Software

**[TalentYak](https://github.com/Niyog59/TalentYak)**, an independent project. A fitness coaching
platform for Nepali coaches and clients abroad that I designed and built on my own with Next.js,
TypeScript, and Supabase PostgreSQL. Most of the interesting work was on the data side: row-level
security so people only see their own records, integer money math with tests, and payment
events that are safe to receive twice. It is still in development with a test site; it is not
open to customers and handles no real payments.
<a href="https://github.com/Niyog59/TalentYak/blob/main/docs/PORTFOLIO.md">Technical overview</a>

<sub>I also built [MeetMerchants](https://meetmerchants.com), a B2B marketplace for businesses and suppliers in Nepal.</sub>

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
