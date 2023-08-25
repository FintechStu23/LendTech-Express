# LendTech-Express (Mortage Loan Application Chatbot)

## Blending "Lending" and "Technology" to showcase the tech-driven efficiency of our mortgage approval bot!

### The project involves the development of a mortgage loan approval application using Python's Streamlit framework. The application allows customers to submit loan applications through a chatbot interface. Additionally, a smart contract for loan approval is created using the REMIX IDE, enabling automated decision-making on loan applications. 

### This project intersects with fintech by leveraging cutting-edge technologies to streamline traditional financial processes. Fintech emphasizes the integration of technology to enhance financial services, and our project exemplifies this by utilizing Streamlit's interface and smart contracts to optimize the mortgage loan approval process.

### Project Goals
* Develop a user-friendly mortgage loan application interface using Python's `Streamlit` framework

* Implement a `smart contract` on the `REMIX IDE` for automated loan approval or denial.

* Showcase the synergy between modern technology (`Streamlit`) and blockchain (`smart contracts`) in the fintech domain.


### Project Concepts:
* Develop a chatbot using a platform like Dialog Flow, Botpress, or Rasa. Design the conversation flow to gather necessary information from the user, such as personal details, financial history, and desired loan terms.

* Integrate Chatbot with Smart Contract:Set up communication between the chatbot and the smart contract. When a user submits a mortgage application through the chatbot, the chatbot should trigger a transaction on the blockchain to submit the application to the smart contract.

* Automated Application Review: Implement logic in the smart contract to automatically review the application based on predefined criteria. The smart contract can calculate the applicant's creditworthiness, evaluate income, and compare against predefined thresholds.

* Notification and Approval Process: Once the application is reviewed, the smart contract can notify the chatbot about the approval status. The chatbot can then inform the user about the decision and provide relevant details.

* Transparency and Auditability: As the smart contract's actions are recorded on the blockchain, the entire mortgage approval process becomes transparent and auditable. Users can verify the process and approvals at any time.

* Handle Payments and Escrow: If the loan is approved, you can include logic in the smart contract for handling loan payments and escrow. Payments can be automatically deducted based on the terms specified in the smart contract.

* User Queries and Support: Design the chatbot to handle user queries related to the mortgage process, repayment schedule, and other relevant information.

* Testing and Deployment: Thoroughly test the integration between the chatbot and the smart contract. Deploy the smart contract to the chosen blockchain network and make the chatbot accessible to users.

### Project Flowchart



### General Objective: Design the Smart Contract

* Streamlit Interface
We used Python and Streamlit to create a user-friendly chatbot-based interface for loan applications, capturing essential applicant information.

* Streamlit UI
A faster way to build and share data apps. Streamlit turns data scripts into shareable web apps in minutes. All in pure Python. No front‑end experience is required. Streamlit is an open-source Python library that can build a UI for various purposes, it is not limited to data apps/machine learning. It is easy to learn, and a few lines of code can create a beautiful web app

The Streamlit app can take user inputs, call contract functions, and display the results.
Please note that this approach requires a two-step process: first deploying the contract in Remix and then building a separate Streamlit app to interact with the deployed contract. The Streamlit app communicates with the contract on the Ethereum network using the contract's ABI and address.

* Blockchain
A blockchain is a distributed database or ledger shared among a computer network's nodes. They are best known for their crucial role in cryptocurrency systems for maintaining a secure and decentralized record of transactions, but they are not limited to cryptocurrency uses. Blockchains can be used to make data in any industry immutable—the term used to describe the inability to be altered.

Blockchain is ideal for delivering that information because it provides immediate, shared, and completely transparent information stored on an immutable ledger that can be accessed only by permissioned network members. A blockchain network can track orders, payments, accounts, production and much more.

The use of credit scoring, pay slips, and bank statements may become increasingly less important to approve a loan. Thanks to smart contracts, lenders are able to validate transactions, verify the legitimacy of counterparties, and perform routine account administration tasks almost momentarily, reducing costs and accelerating the process.

We selected a blockchain platform that supports the development and deployment of smart contracts. Ethereum is selected due to its robust smart contract capabilities.

* Ethereum
Ethereum is the community-run technology powering the cryptocurrency ether (ETH) and thousands of decentralized applications. Cryptocurrencies, such as Bitcoin, enable anyone to transfer money globally. Ethereum does, too, but it can also run code that enables people to create apps and organizations. It’s both resilient and flexible: any computer program can run on Ethereum. Ether (ETH) is the currency powering the Ethereum network and apps.

* Solidity
Solidity is a statically typed programming language designed for developing smart contracts that run on the Ethereum Virtual Machine (EVM) or compatible virtual machines. Solidity uses ECMAScript -like syntax which makes it familiar for existing web developers; however, unlike ECMAScript it has static typing and variadic return types.

* Remix IDE
To create smart contracts on the Ethereum blockchain, developers require an environment that simplifies the development process, provides useful tools and features, and streamlines the testing and debugging of smart contracts. Remix IDE fulfills these requirements and is widely used by developers for Solidity Smart Contract Development.

Remix IDE is a powerful and popular Integrated Development Environment (IDE) for Solidity Smart Contract Development. It is a web-based IDE that allows developers to write, test, debug, and deploy smart contracts on the Ethereum blockchain. Remix IDE provides a user-friendly interface that simplifies the Solidity development process, making it accessible to developers of all skill levels.
To incorporate real-world data into your smart contract, you can use Chain Link oracles to fetch external data (such as current interest rates) onto the blockchain for calculations.

* Smart Contract Development
In the REMIX IDE, we wrote a smart contract that evaluates loan applications based on predefined criteria and automatically approves or denies the application.

Write the smart contract code using a programming language like Solidity (for Ethereum). Include functions for submitting mortgage applications, reviewing applications, calculating payments, and updating approval status.

* Smart Contract
A smart contract is a self-executing program that automates the actions required in an agreement or contract. Contracts execute themselves and transactions happen automatically when both parties meet the conditions specified as part of a transaction. The executed contract then adds on to the blockchain as a transaction. Once completed, the transactions are trackable and irreversible. Smart contracts permit trusted transactions and agreements to be carried out among disparate, anonymous parties without the need for a central authority, legal system, or external enforcement mechanism. Smart Contracts are indispensable to blockchain and vice-versa, as the execution happens because and through the blockchain technology. It is the digital identity that enables smart contracts as a technology. While blockchain technology has come to be thought of primarily as the foundation for Bitcoin, it has evolved far beyond underpinning a virtual currency.

The Streamlit app can take user inputs, call contract functions, and display the results.
Please note that this approach requires a two-step process: first deploying the contract in Remix and then building a separate Streamlit app to interact with the deployed contract. The Streamlit app communicates with the contract on the Ethereum network using the contract's ABI and address.

The smart contract structure will handle the loan mortgage approval process. The smart contract will store relevant information such as applicant details, loan terms, and approval status.

* Chatbot Interface
A chatbot user interface (UI) is the layout of the chatbot software that a user sees and interacts with. It includes chat widget screens, a bot editor’s design, and other visual elements like images, buttons, and icons. All these indicators help a person get the most out of the chatbot tool if done right.

- Insight - Integrating smart contracts into financial applications enhances transparency and security.

- Challenge - Ensuring that the smart contract logic covers all relevant criteria for loan approval.

- Results - The mortgage loan approval application successfully integrates Streamlit's intuitive UI with smart contracts for automated decision-making.

- Conclusion - The project demonstrates how fintech can revolutionize traditional financial processes, making them more efficient and reliable.

- Scalability - Adapt the application for handling a larger volume of loan applications simultaneously.

- Machine Learning - Incorporate machine learning algorithms to enhance the accuracy of loan approval decisions.
Real Data - Connect the application to real-world financial data for more robust testing.
Security Audit - Conduct a thorough security audit of the smart contract to identify vulnerabilities.

## If granted additional time, we would delve into:

* Risk Assessment - Developing a risk assessment model to evaluate the financial stability of applicants.

* Regulatory Compliance - Ensuring the smart contract aligns with relevant financial regulations.

* User Experience Enhancement - Continuously refining the Streamlit interface based on user feedback, including install payment calculations.

