# Citibike Data Pipeline with Databricks and CI/CD


## Objective

* Connect to Databricks using Databricks Connect and run PySpark jobs locally.

* Use Databricks CLI to initialize, configure, and deploy across the Medallion Architecture.

* Package notebooks, scripts, jobs, and cluster configs into a Databricks Asset Bundle (DAB).

* Integrate with GitHub and implement full CI/CD workflows using GitHub Actions for automated testing and deployment.

## Pipeline Architecture: Medallion Model

Using the Citibike dataset, the pipeline follows a Medallion architecture:

- Bronze Layer
  * Ingests citibike raw data
  * Registers metadata in Unity Catalog for data governance and lineage tracking
- Silver Layer
  * Refines data by
    * Computing trip durations
    * Converting timestamp fields into standard date formats
- Gold Layer
  * Delivers analytical insights
    * Trip duration analysis by ride_id type
    * Aggregated trip durations by stationand trip start date

## Development Strategy
Two versions of the pipeline are maintained

1. Notebook Version (.ipynb)
   * Interactive development
2. Script Version (.py)
   * Sutiable for production deployment
   * Supports Version Control, Modularity, Automation and CI/CD integration
     
**Local Development using Databricks Connect and PySpark are deployed**

## CI/CD Workflow
1. Initialize the Databricks Asset Bundle (DAB) in your local development environment.
2. Push the project to a remote GitHub repository to enable version control.
3. There are three workspaces:
   * Dev Workspace: For isolated testing of DAB bundle iterations
   * Test Workspace: For integration testing and data quality validation
   * Prod Workspace: For final deployment after approval
4. On push, the CI pipeline is triggered:
   * Checks out code
   * Installs dependencies
   * Runs unit tests
5. Upon successful CI:
   * A Pull Request(PR) is opened to merge changes into the main branch
6. After merging:
   * The CD pipeline is triggered
   * Automatically deploys the versioned bundle into the Test environment
7. The workflow pauses at a protected approval gate.
8. Once approved by a stakeholder, deployment continues into Production, using the same bundle.

## Features Used
1. Databricks CLI & DAB commands
2. Local Development with Databricks Connect
3. Local Development with PySpark
4. Unit Testing
5. GitHub Integration
6. CI/CD with GitHub Actions
7. Azure Service Principal (ASP) for Test and Prod workspaces
8. Personal Access Tokens (PATs) to each deployment for Dev workspaces

