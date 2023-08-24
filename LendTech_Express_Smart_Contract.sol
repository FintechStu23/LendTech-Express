pragma solidity ^0.5.0;

contract LoanApprovalContract {
    address public owner;

    enum ApplicationStatus { Pending, Approved, Denied }

    struct LoanApplication {
        uint256 age;
        uint256 income;
        uint256 loan_amount;
        uint256 loan_term;
        uint256 credit_score;
        string loan_purpose;
        bool has_existing_loan;
        ApplicationStatus status;
    }

    mapping(address => LoanApplication) public applications;

    constructor() public {
        owner = msg.sender; 
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    function submitApplication(
        uint256 _age,
        uint256 _income,
        uint256 _loanAmount,
        uint256 _loanTerm,
        uint256 _creditScore,
        string calldata _loanPurpose,
        bool _hasExistingLoan
    ) external {
        applications[msg.sender] = LoanApplication({
            age: _age,
            income: _income,
            loan_amount: _loanAmount,
            loan_term: _loanTerm,
            credit_score: _creditScore,
            loan_purpose: _loanPurpose,
            has_existing_loan: _hasExistingLoan, 
            status: ApplicationStatus.Pending
        });
    }

    function approveApplication(address _applicant) external onlyOwner {
        applications[_applicant].status = ApplicationStatus.Approved;
    }

    function denyApplication(address _applicant) external onlyOwner {
        applications[_applicant].status = ApplicationStatus.Denied;
    }

    function getApplicationStatus() external view returns (ApplicationStatus) {
        return applications[msg.sender].status;
    }


}
