import os

# Define the content for the report
report_content = """
# **EV Analysis Report**

<br>

## <i><ins>`PRIMARY ANALYSIS`</ins></i>

### `1. Top 3 and Bottom 3 Makers for 2-Wheelers`

### **FY 2023 - Top 3 Makers:**

| **Fiscal Year** | **Maker**       | **Electric Vehicles Sold** |
|-----------------|-----------------|----------------------------|
| 2023            | **OLA ELECTRIC**| 152,583                    |
| 2023            | **OKINAWA**     | 96,945                     |
| 2023            | **HERO ELECTRIC**| 88,993                    |

### **FY 2024 - Top 3 Makers:**

| **Fiscal Year** | **Maker**       | **Electric Vehicles Sold** |
|-----------------|-----------------|----------------------------|
| 2024            | **OLA ELECTRIC**| 322,489                    |
| 2024            | **TVS**         | 180,743                    |
| 2024            | **ATHER**       | 107,552                    |

### **FY 2023 - Bottom 3 Makers:**

| **Fiscal Year** | **Maker**       | **Electric Vehicles Sold** |
|-----------------|-----------------|----------------------------|
| 2023            | **JITENDRA**    | 8,563                      |
| 2023            | **BEING**       | 11,018                     |
| 2023            | **PURE EV**     | 11,556                     |

### **FY 2024 - Bottom 3 Makers:**

| **Fiscal Year** | **Maker**            | **Electric Vehicles Sold** |
|-----------------|----------------------|----------------------------|
| 2024            | **BATTRE ELECTRIC**  | 4,841                      |
| 2024            | **REVOLT**           | 7,254                      |
| 2024            | **KINETIC GREEN**    | 9,585                      |

---

<br>

### `2. Top 5 States with Highest Penetration Rate in FY 2024`

### **2-Wheelers:**

| **State**       | **Penetration Rate (%)** |
|-----------------|--------------------------|
| **Goa**         | 18.18                    |
| **Kerala**      | 13.61                    |
| **Karnataka**   | 11.51                    |
| **Maharashtra** | 10.16                    |
| **Delhi**       | 9.70                     |

### **4-Wheelers:**

| **State**       | **Penetration Rate (%)** |
|-----------------|--------------------------|
| **Kerala**      | 42.31                    |
| **Chandigarh**  | 4.91                     |
| **Goa**         | 4.37                     |
| **Karnataka**   | 4.28                     |
| **Delhi**       | 4.26                     |

---

<br>

### `3. States with Negative Penetration in EV Sales (2022-2024)`

| **State**                   | **Penetration Change (%)** |
|-----------------------------|----------------------------|
| **Andaman & Nicobar Island**| -0.06                       |
| **Ladakh**                  | -0.62                       |

---

<br>

### `4. Quarterly Trends of Top 5 EV Makers (4-Wheelers) from 2022 to 2024`

![Quarterly Sales for FY 2022-2024 for Top-5 makers of 4-wheeler EVs](./output-4.png)

---

<br>

### `5. Comparison of EV Sales and Penetration Rate in Delhi vs Karnataka for 2024`

### **EV Sales in 2024:**

- **Delhi:** 46,724 vehicles
- **Karnataka:** 160,989 vehicles

### **Penetration Rate in 2024:**

- **Delhi:** 6.98%
- **Karnataka:** 7.89%

---

<br>

### `6. Compounded Annual Growth Rate (CAGR) in 4-Wheeler Units for Top 5 Makers from 2022 to 2024`

| **Maker**                | **CAGR (2022-2024) (%)** |
|--------------------------|--------------------------|
| **BYD India**            | 5.67                     |
| **Hyundai Motor**        | 2.55                     |
| **MG Motor**             | 1.32                     |
| **Mahindra & Mahindra**  | 1.40                     |
| **Tata Motors**          | 0.95                     |

---

<br>

### `7. Top 10 States with the Highest CAGR from 2022 to 2024 in Total Vehicles Sold`

| **State**           | **CAGR (2022-2024) (%)** |
|---------------------|--------------------------|
| **Meghalaya**       | 28.47                     |
| **Goa**             | 27.41                     |
| **Karnataka**       | 25.28                     |
| **Delhi**           | 22.88                     |
| **Rajasthan**       | 21.50                     |
| **Gujarat**         | 20.55                     |
| **Assam**           | 20.13                     |
| **Mizoram**         | 18.77                     |
| **Arunachal Pradesh**| 18.30                    |
| **Haryana**         | 17.68                     |

---

<br>

### `8. Peak and Low Season Months for EV Sales (2022-2024)`

- **Peak Sales Month:** **March** (291,587 EVs sold)
- **Low Sales Month:** **June** (106,709 EVs sold)

### **Month-wise Sales (Sorted High to Low)**

| **Month**    | **EVs Sold**   |
|--------------|----------------|
| **March**    | 291,587        |
| **November** | 205,196        |
| **February** | 198,049        |
| **January**  | 189,099        |
| **October**  | 185,185        |
| **December** | 180,401        |
| **May**      | 159,869        |
| **September**| 145,972        |
| **August**   | 141,961        |
| **April**    | 134,657        |
| **July**     | 127,426        |
| **June**     | 106,709        |

![Monthly EV Sales from 2022 to 2024](./output-8.png)

---

<br>

### `9. Projected Number of EV Sales for the Top 10 States by Penetration Rate in 2030`

| **State**        | **Projected Sales (2030)** |
|------------------|----------------------------|
| **Maharashtra**  | 10,745,693                |
| **Karnataka**    | 8,773,886                 |
| **Tamil Nadu**   | 5,140,104                 |
| **Gujarat**      | 4,597,558                 |
| **Kerala**       | 4,029,614                 |
| **Rajasthan**    | 3,621,192                 |
| **Delhi**        | 2,546,453                 |
| **Odisha**       | 2,131,927                 |
| **Goa**          | 588,544                   |
| **Chandigarh**   | 156,796                   |

![Top-10 States by PR in 2030 based on CAGR](./output-9.png)

---

<br>

### `10. Revenue Growth Rate of 4-Wheeler and 2-Wheeler EVs in India for 2022-2024 and 2023-2024`

### **Assumptions:**

| **Vehicle Category** | **Average Price (INR)** |
|----------------------|-------------------------|
| **2-Wheelers**       | 85,000                  |
| **4-Wheelers**       | 15,00,000               |

### **Revenue Growth Rate:**

- **2-Wheelers (2022-2024):** 269.28%
- **2-Wheelers (2023-2024):** 28.13%
- **4-Wheelers (2022-2024):** 367.79%
- **4-Wheelers (2023-2024):** 83.08%

---

<br>

## <i><ins>`SECONDARY ANALYSIS`</ins></i>

To address the secondary questions for AtliQ Motors, I'll provide detailed answers based on the general trends and insights gathered from the Indian EV market, government policies, consumer behavior, and market data:

### 1. Primary Reasons for Customers Choosing 4-Wheeler EVs in 2023 and 2024

**Cost Savings**:  
- **Lower Running Costs**: EVs have significantly lower running costs compared to traditional internal combustion engine (ICE) vehicles. The reduction in fuel expenses, coupled with lower maintenance costs (due to fewer moving parts), makes EVs attractive.
- **Total Cost of Ownership (TCO)**: With rising fuel prices, the TCO of EVs is increasingly favorable, especially with government incentives that reduce the upfront cost of EVs.

**Environmental Concerns**:  
- **Growing Awareness**: There's increasing awareness among consumers about climate change and the environmental impact of fossil fuels. This concern drives eco-conscious consumers to choose EVs to reduce their carbon footprint.
- **Corporate and Social Responsibility**: Many consumers are influenced by the broader societal trend toward sustainability, aligning their purchasing decisions with environmental values.

**Government Incentives**:  
- **Subsidies and Tax Benefits**: Government policies like the Faster Adoption and Manufacturing of Hybrid and Electric Vehicles (FAME) scheme provide direct subsidies to EV buyers. Additionally, reduced road taxes, registration fees, and GST cuts on EVs make them financially appealing.
- **Increased Range and Model Availability**: With more manufacturers entering the EV space, there's a wider selection of models with better range, which addresses the range anxiety concern that earlier limited EV adoption.

### 2. Impact of Government Incentives and Subsidies on Adoption Rates of 2-Wheelers and 4-Wheelers

**Impact on Adoption Rates**:
- **Increased Adoption**: Government incentives have played a crucial role in accelerating EV adoption in India. By lowering the effective purchase price, these subsidies have made EVs more accessible to a broader demographic.
- **Shift in Market Dynamics**: While earlier, EVs were seen as premium products, subsidies have democratized them, leading to increased sales among middle-income households.
- **Preference for 2-Wheelers in Urban Areas**: In urban areas, where traffic congestion and fuel costs are significant concerns, subsidies have led to a surge in the adoption of electric 2-wheelers.

**States Providing the Most Subsidies**:
- **Maharashtra**: Offers substantial subsidies for both 2-wheelers and 4-wheelers under its EV policy, including incentives on vehicle purchase and scrapping of old vehicles.
- **Delhi**: Known for its aggressive EV policies, Delhi offers one of the highest purchase subsidies, especially for 2-wheelers, making it a leader in EV adoption.
- **Gujarat**: Provides significant subsidies under its state EV policy, focusing on both 2-wheelers and 4-wheelers, along with tax exemptions.
- **Karnataka**: Another key state offering considerable incentives, especially for 4-wheelers, aligning with its broader industrial policy to promote electric mobility.

### 3. Correlation Between Charging Infrastructure and EV Sales/Penetration Rates in Top 5 States

**Correlation**:
- **Direct Correlation**: The availability of charging infrastructure is strongly correlated with EV sales and penetration rates. States with more developed charging networks tend to see higher adoption rates, as consumers are less concerned about range anxiety.
- **Top States with Charging Infrastructure**:
  - **Delhi**: Boasts a robust charging network, contributing to its high EV penetration rates.
  - **Maharashtra**: Significant investments in public and private charging infrastructure have supported its high sales figures.
  - **Karnataka**: With its capital, Bengaluru, being an IT hub, the state has seen rapid deployment of charging stations, aiding EV adoption.
  - **Tamil Nadu**: The state's focus on infrastructure development, including charging stations, has been instrumental in driving EV sales.
  - **Gujarat**: Known for its proactive EV policies, Gujarat has invested in expanding its charging network, correlating with high sales penetration.

### 4. Ideal Brand Ambassador for AtliQ Motors' EV/Hybrid Vehicle Launch in India

**Suggested Brand Ambassador**: **Virat Kohli**
- **Reasons**:
  - **Mass Appeal**: As one of India's most popular sports figures, Virat Kohli has a massive following across demographics, making him an ideal choice to connect with a broad audience.
  - **Alignment with Brand Values**: Kohli is known for his focus on fitness, discipline, and modern outlook, which aligns with the values of innovation and sustainability that AtliQ Motors may want to project.
  - **Environmental Advocacy**: Kohli has previously shown support for environmental causes, which could lend credibility to AtliQ Motors' commitment to sustainability.

### 5. Ideal State to Start the Manufacturing Unit

**Recommended State**: **Gujarat**
- **Subsidies and Incentives**: Gujarat offers attractive subsidies for setting up manufacturing units, including capital investment subsidies, interest subsidies, and exemptions from various state taxes.
- **Ease of Doing Business**: Gujarat consistently ranks high on the Ease of Doing Business Index in India, thanks to its efficient bureaucratic processes and business-friendly environment.
- **Stability in Governance**: The state has a reputation for stable governance and proactive industrial policies, making it a preferred destination for large-scale manufacturing operations.
- **Strategic Location**: Proximity to key ports (like Mundra and Kandla) facilitates easy export of vehicles, which is critical for scaling operations.

### 6. Top 3 Recommendations for AtliQ Motors

1. **Focus on Affordability and Range**:
   - **Develop a Competitive Pricing Strategy**: Given the price sensitivity of the Indian market, AtliQ Motors should focus on making EVs affordable while offering competitive ranges to address consumers' primary concerns.
   - **Innovate in Battery Technology**: Investing in R&D to develop or source cost-effective, high-range batteries will be crucial to attracting a broad customer base.

2. **Expand Charging Infrastructure Partnerships**:
   - **Collaborate with Charging Networks**: Partner with established charging infrastructure providers to ensure a seamless experience for customers, especially in top markets like Maharashtra, Delhi, and Karnataka.
   - **Offer Home Charging Solutions**: Provide customers with home charging equipment as part of the purchase package, which can ease the transition to EVs for new adopters.

3. **Leverage Government Incentives**:
   - **Maximize State and Central Government Benefits**: Ensure that AtliQ Motors' products are positioned to fully benefit from available state and central government subsidies, thereby reducing the effective price for consumers.
   - **Advocate for Policy Support**: Engage with policymakers to advocate for favorable EV policies that can drive market growth, such as additional tax breaks, enhanced subsidies, and more charging infrastructure development.

"""

# Save the report content to a markdown file
with open("Codebasics_EV_Analysis_Report.md", "w") as file:
    file.write(report_content)

print("Report has been generated successfully as 'Codebasics_EV_Analysis_Report.md'.")