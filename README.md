# 02268POESS
DTU Project Material for course 02268 Process Oriented and Event Driven Software Systems

## Description of the Project

### Overview
The project focuses on optimizing the public transportation system, specifically the bus operations of Movia, a leading public transport provider in Denmark. The primary goal is to **maximize passenger capacity on each bus while ensuring complete route coverage**. The approach combines **Business Process Model and Notation (BPMN)**, **Complex Event Processing (CEP)**, and supporting technologies to analyze and optimize key operational processes. The initiative is driven by the importance of public transit in urban areas, aiming to improve efficiency, reliability, and sustainability.

---

### Key Processes
#### Core Processes
1. **Rerouting Buses**: 
   - Real-time adjustments to routes in case of delays or disruptions (e.g., traffic accidents).
   - Integration of predictive engines and automated escalation for resource allocation.
   - Feedback mechanisms for improving future rerouting predictions.

2. **Dispatching Buses**: 
   - Responding to demand spikes with available buses and drivers.
   - Continuous monitoring of demand spikes to adjust routes dynamically.

#### Support Processes
1. **Maintain Buses**: 
   - Routine maintenance and diagnostics handled by mechanics.
   - Classification of repairs as minor or major, with approval workflows for significant issues.
   
2. **Clean Buses**:
   - Interior and exterior cleaning processes to ensure passenger satisfaction.
   - Quality checks before returning buses to service.
   
3. **Hire Drivers**:
   - Systematic candidate evaluation, training, and readiness assessment to ensure operational consistency.

#### Management Processes
1. **Review Guidelines**:
   - Periodic updates and compliance checks to align operations with industry standards.
   - Stakeholder workshops and iterative improvements.

2. **Ensure Coverage**:
   - Geographical analysis to identify service gaps.
   - Proposal and implementation of new routes based on resource feasibility.

---

### Event Management
#### Event Sources
- **Traffic Events**: Simulated traffic disruptions (e.g., accidents, road closures) with attributes like impact level, affected buses, and closure status.
- **Climate Events**: Environmental disruptions (e.g., snow, floods) with parameters like location, impact level, and precipitation.

#### Event Processing
- Events are generated using Python scripts or HTTP POST requests.
- **Siddhi CEP Engine**:
  - **Traffic Events**: Handled by "AccidentApp" to determine high-impact disruptions.
  - **Climate Events**: Managed by "ClimateApp" to identify extreme weather scenarios.
- Events triggering high-impact levels initiate workflows in the **Camunda BPM engine** for actions like rerouting or rescheduling.

---

### Tools and Technologies Used
1. **BPMN**:
   - Modeled processes like rerouting, dispatching, cleaning, and maintenance.
   - Used to define workflows and interactions among stakeholders.
2. **Complex Event Processing (CEP)**:
   - Siddhi engine for real-time event monitoring and processing.
3. **Python Scripts**:
   - Generating traffic and climate event data.
   - HTTP server to serve JSON-formatted events for CEP.
4. **Camunda BPM**:
   - Workflow engine to handle rerouting and rescheduling processes.
5. **Postman**:
   - Manual event creation and testing.

---

### Limitations
- **System Complexity**: Increased difficulty in maintaining and modifying processes as system scope expands.
- **Latency Challenges**: Network delays or slow event processing can affect real-time decision-making.
- **Scalability**: Performance issues with CEP under heavy event loads.

---

### Practical Implications
The envisioned system improves operational efficiency, reduces environmental impact, and enhances passenger satisfaction by leveraging automation, real-time analytics, and advanced event-driven systems. However, scalability and flexibility remain key challenges as the system evolves to accommodate real-world complexities.
