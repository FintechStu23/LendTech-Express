import streamlit as st
from web3 import Web3

# Initialize Web3 and connect to the contract
web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))
contract_address = "0xa1311ECcEd67c0b9ED41c55B5a8B893cf1712CE8"
contract_abi =[
	{
		"inputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"constant": True,
		"inputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"name": "applications",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "age",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "income",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "loan_amount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "loan_term",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "credit_score",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "loan_purpose",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "has_existing_loan",
				"type": "bool"
			},
			{
				"internalType": "enum LoanApprovalContract.ApplicationStatus",
				"name": "status",
				"type": "uint8"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "address",
				"name": "_applicant",
				"type": "address"
			}
		],
		"name": "approveApplication",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "address",
				"name": "_applicant",
				"type": "address"
			}
		],
		"name": "denyApplication",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": False,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "_age",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_income",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_loanAmount",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_loanTerm",
				"type": "uint256"
			},
			{
				"internalType": "uint256",
				"name": "_creditScore",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "_loanPurpose",
				"type": "string"
			},
			{
				"internalType": "bool",
				"name": "_hasExistingLoan",
				"type": "bool"
			}
		],
		"name": "submitApplication",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]  # Your contract's ABI

# Connect to the contract
contract = web3.eth.contract(address=contract_address, abi=contract_abi)


# Streamlit Application
st.title("LendTech-Express")

# Add the image
image_url = "https://empire-s3-production.bobvila.com/articles/wp-content/uploads/2022/02/The-Best-Mobile-Home-Loans-Options-650x434.jpg"
st.image(image_url, use_column_width=True)


# Personal Information
st.header("Personal Information")
name = st.text_input("First Name, Last Name:")
age = st.number_input("Age:", min_value=18, max_value=100)
email = st.text_input("Email:")
phone = st.text_input("Phone:")

# Employment Information
st.header("Employment Information")
employer_name = st.text_input("Employer Name:")
job_title = st.text_input("Job Title:")
income = st.number_input("Monthly Income ($):", min_value=0)
annual_gross_income = income * 12
formatted_income = "${:,.2f}".format(annual_gross_income)
st.write("Annual Gross Income:", formatted_income)

# Loan Details
st.header("Loan Details")
loan_amount = st.number_input("Requested Loan Amount ($):", min_value=0)
loan_term = st.selectbox("Loan Term (years):", [10, 15, 20, 25, 30])
credit_score = st.slider("Credit Score:", min_value=300, max_value=850)

# Loan Purpose and Additional Information
st.header("Other Information")
loan_purpose = st.text_area("Loan Purpose:")
has_existing_loan = st.checkbox("Do you have an existing loan?")
additional_info = st.text_area("Additional Information:")


application_status = None

# from Ganache
user_address = '0xcBFe3fBF44F93F447a3663FF003b154b7a565d30'
pk = '0x9d4797d58558586a4e74afb6aec3faba796a3ecd9688132101eef8605cf7ba1f'

if st.button("Submit Application"):
   try: 
      if not name or not age or not email or not phone or not employer_name or not job_title or not credit_score or not loan_purpose or not loan_term or income <= 0 or loan_amount <= 0:
        st.error("Please fill in all required fields before submitting.")

      else:
        # Prepare the transaction and send it to the Smart Contract
        tx_hash = contract.functions.submitApplication(
            age,
            income,
            loan_amount,
            loan_term,
            credit_score,
            loan_purpose,
            has_existing_loan
        ).transact({'from': user_address})

        st.success("Your loan application has been successfully submitted!")
        st.write("Transaction hash:", tx_hash.hex())    


   except Exception as e:
        st.error(f"An error occurred: {str(e)}")


with st.sidebar:
        st.write("Contact us:")
        st.write("Phone: 999-LendTech-Express")
        st.write("Email: lendtech.express@gmail.com")


st.write("---")   

# Add a button to check application status
check_status_button = st.button("Check Your Loan Application Status")

# Retrieve application status from smart contract
   
if check_status_button:   
   try:
       application_status = contract.functions.applications(user_address).call()

      # Display application status
       if application_status[7] == 0:  # Assuming ApplicationStatus.Pending is 0
           st.warning("Your loan application is still pending approval.")
       elif application_status[7] == 1:  # Assuming ApplicationStatus.Approved is 1
           st.success("Congratulations! Your loan application has been approved!")
       elif application_status[7] == 2:  # Assuming ApplicationStatus.Denied is 2
           st.error("We are sorry! Your loan application has been denied. Please contact us if you have any questions.")
       else:
           st.warning("Application status is not recognized.")

   except Exception as e:
       st.error(f"Error retrieving application status: {str(e)}")
       application_status = None
