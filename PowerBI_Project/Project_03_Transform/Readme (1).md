# Northstar Bank: From UAT Readiness to Service Request Performance
Power BI | Business Analysis | Business Intelligence | Data Visualisation | UAT

## Project Overview

This project uses a simulated banking dataset and Microsoft Power BI to demonstrate how business requirements, User Acceptance Testing (UAT), defect tracking, and service-request operations can be brought together in an interactive reporting solution.

The project addresses two connected business problems:

1. **Change and testing visibility:** How can a business and testing team monitor requirements coverage, test execution progress, pass rates, and defects before considering a change ready?
2. **Service operations visibility:** How can an operations team monitor service-request volumes, resolution performance, and SLA outcomes across categories, priorities, branches, and assigned teams?

The central business question is:

**How can a consolidated dashboard help stakeholders identify UAT execution risks and understand where service-request operations may require further investigation?**

The report contains two pages: a UAT Executive Dashboard and a Service Request Operations dashboard. The first focuses on requirements traceability and testing outcomes; the second focuses on operational performance and SLA monitoring.

> **Simulation notice:** Northstar Bank is a fictional case-study name. All records, requirements, test cases, defects, and results in this project are simulated for learning and portfolio demonstration. They are not real bank/customer data, production performance figures, or evidence of UAT conducted at a financial institution.

## Tools and Technologies

- Microsoft Power BI Desktop
- Microsoft Excel (source data)
- Power Query (data preparation, where applicable)
- DAX (measures and calculated column)
- Data modelling and relationships
- Simulated banking service-request and UAT dataset

## Dataset

The Excel workbook contains six sheets:

- `Service_Requests`
- `Requirements`
- `UAT_Test_Cases`
- `Defects`
- `Process_Stages`
- `Read_Me`

The simulated dataset contains 500 service-request records, 10 business requirements, 20 UAT test cases, and 4 defect records.

The project uses synthetic data only. No real customer, employee, account, or confidential banking information is included.

## Dashboard Components

### 1. UAT Executive Dashboard

Provides a management-level view of requirements, test execution, pass rate, and defects.

**Key Performance Indicators**

- Total Requirements: 10
- Total Test Cases: 20
- Passed Tests: 9
- Pass Rate: 45%
- Open Defects: 4

**Visualisations**

- UAT Test Execution Status distribution.
- Defect Distribution by Severity.
- Requirements Traceability and Test Coverage table.
- Defect Details table.

The execution-status distribution is:

- Passed: 9
- Failed: 4
- Not Run: 3
- Blocked: 4

The pass rate is calculated as 9 passed test cases divided by 20 total test cases. Open Defects counts defects with a status of `Open` or `In Progress`.

### 2. Service Request Operations Dashboard

Provides an operational view of request volumes, service status, resolution time, and SLA outcomes.

**Key Performance Indicators**

- Total Service Requests: 500
- Resolved Requests: 280
- SLA Breaches: 141
- Average Resolution Time: 3 days (displayed rounded to whole days)

**Visualisations**

- Service Request Status Distribution.
- Service Requests by Category.
- Average Resolution Time by Priority.
- SLA Performance by Assigned Team.
- Interactive filters for Category, Priority, and Branch.

The SLA-by-team visual compares request counts across SLA classifications for each assigned team. It is a count-based comparison, not an SLA compliance percentage.

### 3. Data Model and Business Logic

The report connects requirements to test cases and test cases to defects:

- `Requirements[Requirement_ID]` → `UAT_Test_Cases[Requirement_ID]` (one-to-many).
- `UAT_Test_Cases[Test_ID]` → `Defects[Test_ID]` (one-to-many).

A direct Defects-to-Requirements relationship is not used, avoiding an ambiguous filter path.

The `SLA_Breached` calculated column applies the following rule:

- `Not Yet Resolved` when `Resolution_Time_Days` is blank.
- `Yes` when `Resolution_Time_Days` is greater than `SLA_Target_Days`.
- `No` when `Resolution_Time_Days` is less than or equal to `SLA_Target_Days`.

The SLA Breaches KPI counts records classified as `Yes`. The result of 141 is therefore based on this explicit project rule. It should not be interpreted as a verified bank SLA policy.

## Interactivity

The dashboard provides interactive visual analysis:

- Category, Priority, and Branch slicers allow users to filter service-request information.
- Selecting a status, category, priority, or assigned team can help users examine related operational results through Power BI cross-filtering, subject to the report's visual interactions.
- The UAT page presents requirements, test cases, execution statuses, and defects in connected views through the data model.

The slicers should be tested in the saved report to confirm that they affect the intended visuals.

## Business Questions

- How many requirements and UAT test cases are represented in the testing scope?
- What proportion of test cases have passed?
- How many test cases are failed, blocked, or not yet run?
- How many defects remain open or in progress?
- How many service requests are recorded, and how many have been resolved?
- Which service-request categories account for the greatest volume?
- How does average resolution time vary by priority?
- How are SLA classifications distributed across assigned teams?
- How do category, priority, and branch filters change the operational view?

## Key Findings and Business Inference

The dashboard provides two complementary perspectives: change/testing visibility and service operations visibility.

### UAT and Defect Management

**Requirements and Test Scope:** The simulated project contains 10 requirements and 20 test cases, providing a basis for requirements-to-test traceability.

**Test Execution:** 9 of 20 test cases are marked Passed, resulting in a 45% pass rate. The remaining 11 cases are recorded as Failed, Blocked, or Not Run. This indicates that the simulated test cycle has outstanding work and should not be treated as fully passed.

**Defect Visibility:** The dashboard reports 4 open or in-progress defects. These records should be reviewed and prioritised alongside failed or blocked test cases. The dashboard is intended to make the relationship between requirements, test cases, and defects easier to inspect.

### Service Request Operations

**Service Volume:** The dataset contains 500 service requests, of which 280 are marked Resolved. This represents 56% of all recorded requests.

**SLA Outcomes:** 141 records are classified as SLA breaches under the calculated rule comparing resolution days with the target days. This is a breach count, not a breach rate. Requests without a recorded resolution time are classified separately as `Not Yet Resolved`.

**Category and Priority Analysis:** The category chart compares request volumes across categories, while the priority chart compares average resolution time across priority levels. These views help identify areas for further investigation; the exact causes of differences cannot be established from the dashboard alone.

**Assigned-Team Analysis:** The SLA-by-team chart compares counts by SLA classification. It can help identify where further team-level investigation may be useful, but request volumes and unresolved requests should be considered before drawing conclusions about team performance.

## Answer to the Central Business Question

**How can a consolidated dashboard help stakeholders identify UAT execution risks and understand where service-request operations may require further investigation?**

The dashboard brings together key indicators that would otherwise need to be reviewed across separate registers and operational summaries. The UAT page makes the test pass rate, outstanding execution statuses, requirements traceability, and open/in-progress defects visible in one place. The operations page summarises service volumes, resolved requests, SLA breach counts, resolution time by priority, and SLA classifications by assigned team.

In this simulated snapshot, the 45% UAT pass rate and the presence of failed, blocked, and not-run tests highlight the need for further test-cycle follow-up. In operations, 280 of 500 requests are resolved and 141 are classified as SLA breaches under the project's calculation rule. These figures identify areas to investigate, but do not by themselves explain the causes or establish whether a real service team is meeting its contractual obligations.

Therefore, the dashboard supports structured monitoring and investigation; it does not replace root-cause analysis, stakeholder validation, or formal UAT sign-off.

## Business Recommendations

- Review failed and blocked UAT cases and assign clear owners and next actions.
- Schedule execution or formal disposition of test cases marked Not Run.
- Review the four open or in-progress defects for severity, business impact, ownership, and retest status.
- Maintain traceability from each business requirement to its test cases and related defects.
- Investigate the 141 SLA-classified breach records to understand the reasons for delays.
- Review high-volume service categories to identify opportunities for process improvement.
- Compare resolution time across priority levels and validate whether service targets are appropriate.
- Use the assigned-team comparison as a starting point for investigation, taking request volume and not-yet-resolved cases into account.
- Validate the SLA definition with business stakeholders before applying this logic to real operational data.

## Conclusion

A useful Business Analysis dashboard should connect business requirements and testing outcomes with the operational measures that matter to stakeholders. This project demonstrates that approach through a two-page Power BI report combining UAT traceability, defect monitoring, service-request analysis, and SLA classification.

The findings are based entirely on simulated data and are intended to demonstrate analytical thinking, data modelling, KPI development, and business-oriented reporting.

## Project Files

- `.pbix` — Editable Power BI dashboard.
- `.pdf` — Exported dashboard report.
- `.xlsx` — Simulated source workbook.
- `README.md` — Project documentation.

## Dataset

Simulated banking requirements, UAT test cases, defects, process stages, and service-request records created for this portfolio case study.
