import psycopg2
import os

# PostgreSQL connection
DB_NAME = os.getenv("DB_NAME", "sacdap_2")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "123123")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )


enrollments = []
contacts = []

# Course data structure
courses_data = {
    "accounting": {
        "title": "Career in Accounts",
        "description": "Master the fundamentals and advanced concepts of accounting with our comprehensive courses.",
        "courses": [
            {
                "id": "corporate_accountant",
                "name": "Corporate Accountant Training",
                "duration": "6 months (3 phases)",
                "description": "Comprehensive three-phase program covering all aspects of corporate accounting",
                "pdf_resource": None,  # Space for future PDF upload
                "phases": [
                    {
                        "phase": 1,
                        "title": "Foundation Phase",
                        "duration": "2 months",
                        "topics": [
                            "Basic Accounting Principles",
                            "Financial Statements",
                            "Journal Entries",
                            "Ledger Management",
                        ],
                    },
                    {
                        "phase": 2,
                        "title": "Intermediate Phase",
                        "duration": "2 months",
                        "topics": [
                            "Advanced Accounting",
                            "Cost Accounting",
                            "Management Accounting",
                            "Tax Accounting",
                        ],
                    },
                    {
                        "phase": 3,
                        "title": "Advanced Phase",
                        "duration": "2 months",
                        "topics": [
                            "Corporate Finance",
                            "Audit & Assurance",
                            "Financial Analysis",
                            "Real-world Case Studies",
                        ],
                    },
                ],
            },
            {
                "id": "basic_accounting",
                "name": "Basic Accounting",
                "duration": "2 months",
                "description": "Learn the fundamentals of accounting including bookkeeping, financial statements, and basic principles.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "advanced_accounting",
                "name": "Advanced Accounting",
                "duration": "3 months",
                "description": "Advanced topics including consolidation, partnerships, and complex financial transactions.",
                "pdf_resource": None,  # Space for future PDF upload
            },
        ],
    },
    "stock_market": {
        "title": "Career in Stock Market",
        "description": "Learn trading, investment strategies, and market analysis with our expert-designed courses.",
        "courses": [
            {
                "id": "basic_stock_market",
                "name": "Basic of Stock Market",
                "duration": "1 month",
                "description": "Introduction to stock markets, trading fundamentals, and basic investment concepts.",
                "pdf_resource": None,  # Space for future PDF upload
                "highlights": [
                    "Introduction of share market",
                    "Structure of indian securities market",
                    "Corporate action and impact on stock prices",
                    "Key Events and their impact on market",
                    "Risk and benefit of investing in stock",
                ],
            },
            {
                "id": "technical_analysis",
                "name": "Technical Analysis",
                "duration": "2 months",
                "description": "Learn chart patterns, indicators, and technical analysis tools for trading decisions.",
                "pdf_resource": None,  # Space for future PDF upload
                "highlights": [
                    "Introduction of Technical Analysis",
                    "Dow Theory",
                    "Support And Resistance",
                    "Candlesticks",
                    "Technical Indicators And oscillator",
                    "Price Action",
                    "Risk Management",
                    "Trading Plan",
                ],
            },
            {
                "id": "fundamental_analysis",
                "name": "Fundamental Analysis",
                "duration": "2 months",
                "description": "Analyze company financials, market conditions, and economic factors for investment decisions.",
                "pdf_resource": None,  # Space for future PDF upload
                "highlights": [
                    "Quantitative Analysis",
                    "Qualitative Analysis",
                    "Sector analysis",
                    "Company Management Analysis",
                ],
            },
            {
                "id": "trading_strategy_basic",
                "name": "Trading Strategy Basic",
                "duration": "3 months",
                "description": "Advanced trading strategies, risk management, and portfolio optimization techniques.",
                "pdf_resource": None,  # Space for future PDF upload
                "highlights": [
                    "Long Call",
                    "Short Call",
                    "Long Put",
                    "Short Put",
                    # "Advanced trading techniques",
                    # "Portfolio management",
                    # "Risk assessment",
                    # "Real-time trading practice",
                ],
            },
            {
                "id": "trading_strategy_advanced",
                "name": "Trading Strategy Advanced",
                "duration": "3 months",
                "description": "Advanced trading strategies, risk management, and portfolio optimization techniques.",
                "pdf_resource": None,  # Space for future PDF upload
                "highlights": [
                    "Covered Call",
                    "Covered Put",
                    "Long Straddle",
                    "Short Straddle",
                    "Long Strangle",
                    "Short Strangle",
                    "Bull Call Spread",
                    "Bull Put Spread",
                    "Bear Call Spread",
                    "Bear Put Spread",
                    "Long Call Condor",
                    "Short Call Condor",
                    "Long Call Butterfly",
                    "Short Call Butterfly",
                    "Collar",
                    "Synthetic Long Call",
                    "Synthetic Long Put",
                ],
            },
        ],
    },
    "it": {
        "title": "Career in IT",
        "description": "Build your technology career with cutting-edge programming and digital skills courses.",
        "courses": [
            {
                "id": "python_programming",
                "name": "Python Programming",
                "duration": "3 months",
                "description": "Complete Python programming course from basics to advanced concepts including frameworks.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "web_development",
                "name": "Web Development",
                "duration": "4 months",
                "description": "Full-stack web development including HTML, CSS, JavaScript, and backend technologies.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "data_science",
                "name": "Data Science",
                "duration": "5 months",
                "description": "Learn data analysis, machine learning, and statistical modeling with Python and R.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "digital_marketing",
                "name": "Digital Marketing",
                "duration": "2 months",
                "description": "SEO, social media marketing, content strategy, and online advertising techniques.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "devops",
                "name": "DevOps Engineering",
                "duration": "4 months",
                "description": "Master CI/CD, containerization, automation, and cloud infrastructure management.",
                "pdf_resource": None,  # Space for future PDF upload
            },
            {
                "id": "aws_cloud",
                "name": "AWS Cloud Computing",
                "duration": "3 months",
                "description": "Comprehensive AWS training covering EC2, S3, Lambda, and cloud architecture.",
                "pdf_resource": None,  # Space for future PDF upload
            },
        ],
    },
}


def add_enrollment(data):
    """Add new enrollment to the database"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO enrollments (name, email, phone, course_interested, message)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id;
    """,
        (
            data["name"],
            data["email"],
            data["phone"],
            data["course_interested"],
            data["message"],
        ),
    )
    enrollment_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return enrollment_id


def add_contact(data):
    """Add new contact message to the database"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO contacts (name, email, subject, message)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """,
        (data["name"], data["email"], data["subject"], data["message"]),
    )
    contact_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return contact_id


def get_all_enrollments():
    """Get all enrollments"""
    return enrollments


def get_all_contacts():
    """Get all contact messages"""
    return contacts


def get_course_by_id(course_id):
    """Get course details by ID"""
    for category in courses_data.values():
        for course in category["courses"]:
            if course["id"] == course_id:
                return course
    return None


def get_all_courses_for_search():
    """Get all courses formatted for search dropdown"""
    courses = []
    for category in courses_data.values():
        for course in category["courses"]:
            courses.append(
                {
                    "id": course["id"],
                    "name": course["name"],
                    "category": category["title"],
                }
            )
    return courses
