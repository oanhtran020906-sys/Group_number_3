-- INSERT DATABASE --

USE Employee_Information_Manager;

-- Departments
INSERT INTO Departments (DepartmentName) VALUES
('Data Science'),
('Engineering'),
('Finance'),
('Human Resources'),
('Legal Affairs'),
('Marketing'),
('Sales');

INSERT INTO Employees (EmployeeName, DateOfBirth, DepartmentID) VALUES
('Vũ Thị Nhung', '1990-04-23', 7),  -- ID: 1
('Bùi Minh Quân', '1982-08-19', 3),  -- ID: 2
('Ngô Thị Lan', '1985-12-02', 4),    -- ID: 3
('Hoàng Văn Nam', '1981-01-14', 1),  -- ID: 4
('Trần Thị Thanh', '1983-05-27', 2), -- ID: 5
('Lê Văn Hùng', '1979-09-09', 1),    -- ID: 6
('Phạm Thị Ngọc', '1986-03-05', 3),  -- ID: 7
('Trương Minh Hải', '1984-07-16', 4),-- ID: 8
('Đinh Thị Lan', '1987-12-29', 5),   -- ID: 9
('Nguyễn Văn Sơn', '1979-10-11', 6), -- ID: 10
('Vũ Thị Hương', '1990-02-08', 7),   -- ID: 11
('Bùi Văn Tiến', '1985-06-23', 3),   -- ID: 12
('Ngô Thị Bích', '1989-09-30', 4),   -- ID: 13
('Hoàng Quang Huy', '1982-03-12', 1),-- ID: 14
('Nguyễn Thị Lan', '1984-11-05', 2), -- ID: 15
('Trần Văn Kiên', '1978-04-28', 1),  -- ID: 16
('Lê Thị Hồng', '1986-08-14', 3),    -- ID: 17
('Phạm Văn Cường', '1981-12-07', 4), -- ID: 18
('Đặng Thị Thanh', '1987-05-21', 5), -- ID: 19
('Nguyễn Văn Hòa', '1980-01-19', 6), -- ID: 20
('Vũ Thị Thanh', '1990-07-03', 7),   -- ID: 21
('Bùi Minh Hùng', '1982-09-22', 3),  -- ID: 22
('Ngô Thị Mai', '1985-02-17', 4),    -- ID: 23
('Hoàng Văn Quang', '1981-06-29', 1),-- ID: 24
('Trần Thị Phương', '1983-03-11', 2),-- ID: 25
('Lê Văn Tài', '1979-08-05', 1),     -- ID: 26
('Phạm Thị Hạnh', '1986-12-19', 3),  -- ID: 27
('Trương Minh Tuấn', '1984-05-01', 4),-- ID: 28
('Đinh Thị Nhung', '1987-09-26', 5), -- ID: 29
('Nguyễn Văn Phát', '1979-11-17', 6),-- ID: 30
('Vũ Thị Hồng', '1990-01-30', 7),    -- ID: 31
('Bùi Văn Sơn', '1985-04-14', 3),    -- ID: 32
('Ngô Thị Thanh', '1989-07-21', 4),  -- ID: 33
('Hoàng Quang Vinh', '1982-10-08', 1),-- ID: 34
('Nguyễn Thị Hương', '1984-02-25', 2),-- ID: 35
('Trần Văn Nam', '1978-06-12', 1),   -- ID: 36
('Lê Thị Ngọc', '1986-09-03', 3),    -- ID: 37
('Phạm Văn Minh', '1981-11-18', 4),  -- ID: 38
('Đặng Thị Lan', '1987-04-27', 5),   -- ID: 39
('Nguyễn Văn Tùng', '1980-07-08', 6),-- ID: 40
('Vũ Thị Phương', '1990-12-15', 7),  -- ID: 41
('Bùi Minh Quân', '1982-05-19', 3),  -- ID: 42
('Ngô Thị Hạnh', '1985-08-11', 4),   -- ID: 43
('Hoàng Văn Long', '1981-03-03', 1), -- ID: 44
('Trần Thị Lan', '1983-06-27', 2),   -- ID: 45
('Lê Văn Quang', '1979-10-05', 1),   -- ID: 46
('Phạm Thị Thanh', '1986-01-21', 3), -- ID: 47
('Trương Minh Hùng', '1984-09-14', 4),-- ID: 48
('Đinh Thị Mai', '1987-11-30', 5),   -- ID: 49
('Nguyễn Văn Cường', '1979-05-17', 6),-- ID: 50
('Vũ Thị Lan', '1990-08-02', 7),     -- ID: 51
('Bùi Văn Hòa', '1985-12-23', 3),    -- ID: 52
('Ngô Thị Hồng', '1989-02-06', 4),   -- ID: 53
('Hoàng Quang Nam', '1982-04-28', 1),-- ID: 54
('Nguyễn Thị Thanh', '1984-07-19', 2),-- ID: 55
('Trần Văn Hùng', '1978-11-12', 1),  -- ID: 56
('Lê Thị Phương', '1986-03-30', 3),  -- ID: 57
('Phạm Văn Quý', '1981-06-15', 4),   -- ID: 58
('Đặng Thị Hồng', '1987-09-09', 5),  -- ID: 59
('Nguyễn Văn Minh', '1980-01-27', 6),-- ID: 60
('Vũ Thị Thanh', '1990-05-16', 7),   -- ID: 61
('Bùi Minh Tú', '1982-08-04', 3),    -- ID: 62
('Ngô Thị Mai', '1985-12-10', 4),    -- ID: 63
('Hoàng Văn Tài', '1981-03-21', 1),  -- ID: 64
('Trần Thị Ngọc', '1983-09-09', 2),  -- ID: 65
('Lê Văn Hòa', '1979-06-03', 1),     -- ID: 66
('Phạm Thị Nhung', '1986-11-26', 3), -- ID: 67
('Trương Minh Sơn', '1984-02-14', 4),-- ID: 68
('Đinh Thị Lan', '1987-05-30', 5),   -- ID: 69
('Nguyễn Văn Quý', '1979-08-21', 6),-- ID: 70
('Vũ Thị Hồng', '1990-12-08', 7),    -- ID: 71
('Bùi Văn Dũng', '1985-04-19', 3),   -- ID: 72
('Ngô Thị Thanh', '1989-07-25', 4),  -- ID: 73
('Hoàng Quang Long', '1982-10-02', 1),-- ID: 74
('Nguyễn Thị Lan', '1984-01-15', 2), -- ID: 75
('Trần Văn Phát', '1978-03-28', 1),  -- ID: 76
('Lê Thị Thanh', '1986-06-13', 3),   -- ID: 77
('Phạm Văn Hòa', '1981-09-29', 4),   -- ID: 78
('Đặng Thị Ngọc', '1987-12-05', 5),  -- ID: 79
('Nguyễn Văn Hùng', '1980-05-17', 6),-- ID: 80
('Vũ Thị Mai', '1990-08-30', 7),     -- ID: 81
('Bùi Minh Hòa', '1982-02-09', 3),   -- ID: 82
('Ngô Thị Hạnh', '1985-11-20', 4),   -- ID: 83
('Hoàng Văn Quý', '1981-07-07', 1),  -- ID: 84
('Trần Thị Phương', '1983-10-11', 2),-- ID: 85
('Lê Văn Nam', '1979-01-25', 1),     -- ID: 86
('Phạm Thị Lan', '1986-04-15', 3),   -- ID: 87
('Trương Minh Quang', '1984-08-21', 4),-- ID: 88
('Đinh Thị Thanh', '1987-02-10', 5), -- ID: 89
('Nguyễn Văn Hòa', '1979-12-18', 6), -- ID: 90
('Vũ Thị Hồng', '1990-06-04', 7),    -- ID: 91
('Bùi Văn Minh', '1985-03-28', 3),   -- ID: 92
('Ngô Thị Mai', '1989-09-12', 4),    -- ID: 93
('Hoàng Quang Tài', '1982-05-05', 1),-- ID: 94
('Trần Văn An', '1983-08-15', 2),    -- ID: 95
('Lê Thị Bình', '1986-11-22', 3),    -- ID: 96
('Phạm Văn Chiến', '1981-04-18', 4), -- ID: 97
('Nguyễn Thị Dung', '1984-07-30', 5),-- ID: 98
('Vũ Văn Đạt', '1979-02-14', 6),     -- ID: 99
('Bùi Thị Én', '1990-09-25', 7),     -- ID: 100
('Ngô Văn Phúc', '1982-12-03', 1),   -- ID: 101
('Hoàng Thị Giang', '1985-05-19', 2),-- ID: 102
('Trần Văn Hiếu', '1978-10-08', 3),  -- ID: 103
('Lê Thị Kim', '1986-01-12', 4),     -- ID: 104
('Phạm Văn Lâm', '1983-03-27', 5),   -- ID: 105
('Nguyễn Thị Mỹ', '1984-06-09', 6),  -- ID: 106
('Vũ Văn Nghĩa', '1979-08-23', 7),   -- ID: 107
('Bùi Thị Oanh', '1990-11-17', 1),   -- ID: 108
('Ngô Văn Phong', '1982-07-04', 2),  -- ID: 109
('Hoàng Thị Quỳnh', '1985-02-28', 3),-- ID: 110
('Trần Văn Sỹ', '1978-12-15', 4),    -- ID: 111
('Lê Thị Thu', '1986-04-21', 5),     -- ID: 112
('Phạm Văn Uy', '1983-09-06', 6),    -- ID: 113
('Nguyễn Thị Vân', '1984-01-29', 7), -- ID: 114
('Vũ Văn Xuân', '1979-05-13', 1),    -- ID: 115
('Bùi Thị Yến', '1990-08-07', 2),    -- ID: 116
('Ngô Văn Anh', '1982-03-24', 3),    -- ID: 117
('Hoàng Thị Bích', '1985-10-11', 4), -- ID: 118
('Trần Văn Cảnh', '1978-07-19', 5),  -- ID: 119
('Lê Thị Diệu', '1986-12-02', 6),    -- ID: 120
('Phạm Văn Đức', '1983-02-16', 7),   -- ID: 121
('Nguyễn Thị Hà', '1984-05-08', 1),  -- ID: 122
('Vũ Văn Khánh', '1979-09-30', 2),   -- ID: 123
('Bùi Thị Linh', '1990-04-14', 3),   -- ID: 124
('Ngô Văn Mạnh', '1982-01-27', 4),   -- ID: 125
('Hoàng Thị Ngà', '1985-08-03', 5),  -- ID: 126
('Trần Văn Phú', '1978-11-20', 6),   -- ID: 127
('Lê Thị Quế', '1986-06-25', 7),     -- ID: 128
('Phạm Văn Sang', '1983-03-09', 1),  -- ID: 129
('Nguyễn Thị Trang', '1984-10-22', 2),-- ID: 130
('Vũ Văn Thắng', '1979-07-17', 3),   -- ID: 131
('Bùi Thị Uyên', '1990-02-05', 4),   -- ID: 132
('Ngô Văn Việt', '1982-12-28', 5),   -- ID: 133
('Hoàng Thị Xuân', '1985-05-16', 6), -- ID: 134
('Trần Văn Yên', '1978-09-11', 7),   -- ID: 135
('Lê Thị Ánh', '1986-01-24', 1),     -- ID: 136
('Phạm Văn Bằng', '1983-08-07', 2),  -- ID: 137
('Nguyễn Thị Châu', '1984-03-19', 3),-- ID: 138
('Vũ Văn Dương', '1979-06-02', 4),   -- ID: 139
('Bùi Thị Hạnh', '1990-11-15', 5),   -- ID: 140
('Ngô Văn Khoa', '1982-04-26', 6),   -- ID: 141
('Hoàng Thị Loan', '1985-09-08', 7), -- ID: 142
('Trần Văn Minh', '1978-02-13', 1),  -- ID: 143
('Lê Thị Nga', '1986-07-31', 2),     -- ID: 144
('Phạm Văn Phước', '1983-12-14', 3), -- ID: 145
('Nguyễn Thị Quyên', '1984-05-27', 4),-- ID: 146
('Vũ Văn Sáng', '1979-10-10', 5),    -- ID: 147
('Bùi Thị Thảo', '1990-03-23', 6),   -- ID: 148
('Ngô Văn Trung', '1982-08-06', 7),  -- ID: 149
('Hoàng Thị Vui', '1985-01-18', 1),  -- ID: 150
('Trần Văn Hưng', '1978-04-01', 2),  -- ID: 151
('Lê Thị Kiều', '1986-09-14', 3),    -- ID: 152
('Phạm Văn Lộc', '1983-06-29', 4),   -- ID: 153
('Nguyễn Thị My', '1984-11-12', 5),  -- ID: 154
('Vũ Văn Nhân', '1979-02-25', 6),    -- ID: 155
('Bùi Thị Phúc', '1990-07-08', 7),   -- ID: 156
('Ngô Văn Quyết', '1982-10-21', 1),  -- ID: 157
('Hoàng Thị Sen', '1985-03-04', 2),  -- ID: 158
('Trần Văn Thành', '1978-12-17', 3), -- ID: 159
('Lê Thị Vinh', '1986-05-20', 4);    -- ID: 160

INSERT INTO Projects (ProjectName, ManagerEmployeeID) VALUES
('Economic Policy Research 2024', 2),
('MBA Program Improvement', 2),
('Financial Market Analysis', 2),
('Audit Process Optimization', 2),
('Urban Development Research', 1),
('Academic Administration Management', 1),
('Recruitment and HR Improvement', 1),
('Learning Management Software', 1),
('Data Analytics Platform', 4),
('AI Research Initiative', 4),
('Customer Segmentation Model', 4),
('Predictive Maintenance System', 5),
('Product Design Revamp', 5),
('Quality Assurance Framework', 5),
('Employee Engagement Program', 8),
('Talent Development Plan', 8),
('Legal Compliance Audit', 9),
('Contract Management System', 9),
('Market Expansion Strategy', 10),
('Brand Awareness Campaign', 10),
('Sales Optimization Program', 11),
('Customer Relationship Management', 11),
('Financial Reporting System', 12),
('Risk Management Framework', 12),
('HR Digital Transformation', 13),
('Performance Management System', 13),
('Legal Tech Implementation', 19),
('Corporate Governance Project', 19),
('Digital Marketing Campaign', 20),
('E-commerce Platform', 20),
('Supply Chain Optimization', 21),
('Logistics Management', 21),
('Cloud Migration Project', 24),
('Cybersecurity Initiative', 24),
('Mobile App Development', 25),
('Web Platform Redesign', 25),
('Big Data Infrastructure', 26),
('Machine Learning Models', 26),
('IoT Implementation', 34),
('Smart Factory Project', 34);

INSERT INTO Assignments (EmployeeID, ProjectID, EmployeeRole, Salary) VALUES
(1, 5, 'Coordinator', 12500000), (1, 6, 'Developer', 12500000),
(2, 1, 'Manager', 18000000), (2, 2, 'Team Lead', 18000000),
(3, 15, 'HR Specialist', 14200000), (3, 16, 'Recruiter', 14200000),
(4, 9, 'Data Scientist', 21500000), (4, 10, 'ML Engineer', 21500000),
(5, 12, 'QA Engineer', 16500000), (5, 13, 'Designer', 16500000),
(6, 9, 'Senior Data Scientist', 24500000), (6, 10, 'Research Lead', 24500000),
(7, 1, 'Financial Analyst', 15800000), (7, 3, 'Accountant', 15800000),
(8, 15, 'HR Manager', 15200000), (8, 16, 'Training Coordinator', 15200000),
(9, 17, 'Legal Advisor', 16800000), (9, 18, 'Compliance Officer', 16800000),
(10, 19, 'Marketing Specialist', 14800000), (10, 20, 'Brand Manager', 14800000),
(11, 21, 'Sales Executive', 13500000), (11, 22, 'Account Manager', 13500000),
(12, 23, 'Financial Controller', 17200000), (12, 24, 'Auditor', 17200000),
(13, 25, 'HR Business Partner', 14600000), (13, 26, 'Recruitment Specialist', 14600000),
(14, 27, 'Data Analyst', 20500000), (14, 28, 'BI Developer', 20500000),
(15, 29, 'Software Engineer', 17500000), (15, 30, 'Test Engineer', 17500000),
(16, 31, 'Data Engineer', 22500000), (16, 32, 'Analytics Manager', 22500000),
(17, 33, 'Budget Analyst', 16200000), (17, 34, 'Investment Analyst', 16200000),
(18, 35, 'Compensation Specialist', 15400000), (18, 36, 'Benefits Administrator', 15400000),
(19, 37, 'Corporate Lawyer', 17200000), (19, 38, 'Legal Counsel', 17200000),
(20, 39, 'Digital Marketer', 15200000), (20, 40, 'Content Strategist', 15200000),
(21, 5, 'Sales Manager', 13800000), (21, 6, 'Business Developer', 13800000),
(22, 1, 'Treasury Analyst', 17800000), (22, 4, 'Internal Auditor', 17800000),
(23, 15, 'Talent Acquisition', 14200000), (23, 16, 'HR Coordinator', 14200000),
(24, 9, 'Machine Learning Engineer', 21000000), (24, 10, 'AI Specialist', 21000000),
(25, 12, 'DevOps Engineer', 18000000), (25, 13, 'UX Designer', 18000000),
(26, 10, 'Big Data Engineer', 23500000), (26, 11, 'Data Architect', 23500000),
(27, 2, 'Financial Planner', 16800000), (27, 3, 'Risk Analyst', 16800000),
(28, 15, 'Organizational Development', 15600000), (28, 16, 'HR Consultant', 15600000),
(29, 17, 'Contract Specialist', 17600000), (29, 18, 'Legal Assistant', 17600000),
(30, 19, 'Marketing Analyst', 15600000), (30, 20, 'SEO Specialist', 15600000),
(31, 21, 'Sales Representative', 13200000), (31, 22, 'Client Relations', 13200000),
(32, 1, 'Cost Accountant', 17400000), (32, 4, 'Compliance Auditor', 17400000),
(33, 15, 'HR Generalist', 14400000), (33, 16, 'Training Specialist', 14400000),
(34, 9, 'Data Visualization Expert', 20800000), (34, 11, 'Reporting Analyst', 20800000),
(35, 12, 'Backend Developer', 18200000), (35, 14, 'Automation Engineer', 18200000),
(36, 10, 'NLP Engineer', 22800000), (36, 11, 'Predictive Modeler', 22800000),
(37, 2, 'Management Accountant', 16400000), (37, 3, 'Portfolio Manager', 16400000),
(38, 15, 'Employee Relations', 15800000), (38, 16, 'HRIS Analyst', 15800000),
(39, 17, 'Intellectual Property Lawyer', 17400000), (39, 18, 'Regulatory Affairs', 17400000),
(40, 19, 'Social Media Manager', 15400000), (40, 20, 'Marketing Coordinator', 15400000),
(41, 21, 'Sales Analyst', 13600000), (41, 22, 'Key Account Manager', 13600000),
(42, 1, 'Financial Reporting', 17600000), (42, 4, 'Operational Auditor', 17600000),
(43, 15, 'Recruitment Manager', 14800000), (43, 16, 'HR Director', 14800000),
(44, 9, 'Data Quality Manager', 21200000), (44, 10, 'AI Researcher', 21200000),
(45, 12, 'Frontend Developer', 18400000), (45, 13, 'Product Manager', 18400000),
(46, 10, 'Computer Vision Engineer', 23200000), (46, 11, 'Statistical Analyst', 23200000),
(47, 2, 'Tax Specialist', 16600000), (47, 3, 'Credit Analyst', 16600000),
(48, 15, 'Performance Management', 16200000), (48, 16, 'HR Analytics', 16200000),
(49, 17, 'Labor Lawyer', 17800000), (49, 18, 'Legal Operations', 17800000),
(50, 19, 'Marketing Manager', 15800000), (50, 20, 'Campaign Manager', 15800000),
(51, 21, 'Sales Operations', 13400000), (51, 22, 'Customer Success', 13400000),
(52, 1, 'Business Analyst', 17800000), (52, 4, 'Forensic Auditor', 17800000),
(53, 15, 'Compensation Analyst', 15000000), (53, 16, 'HR Project Manager', 15000000),
(54, 9, 'Database Administrator', 21800000), (54, 11, 'ETL Developer', 21800000),
(55, 12, 'Full Stack Developer', 18800000), (55, 14, 'Security Engineer', 18800000),
(56, 10, 'Deep Learning Engineer', 23800000), (56, 11, 'Quantitative Analyst', 23800000),
(57, 2, 'Mergers & Acquisitions', 17000000), (57, 3, 'Financial Modeling', 17000000),
(58, 15, 'Succession Planning', 16400000), (58, 16, 'Diversity & Inclusion', 16400000),
(59, 17, 'Corporate Governance', 18000000), (59, 18, 'Legal Risk Management', 18000000),
(60, 19, 'Product Marketing', 16200000), (60, 20, 'Market Research', 16200000),
(61, 21, 'Channel Sales', 14000000), (61, 22, 'Partnership Manager', 14000000),
(62, 1, 'Strategic Finance', 18200000), (62, 4, 'IT Auditor', 18200000),
(63, 15, 'HR Technology', 15200000), (63, 16, 'Change Management', 15200000),
(64, 9, 'Cloud Data Engineer', 22200000), (64, 10, 'Robotics Engineer', 22200000),
(65, 12, 'Mobile Developer', 19200000), (65, 13, 'Technical Lead', 19200000),
(66, 10, 'Algorithm Developer', 24200000), (66, 11, 'Business Intelligence', 24200000),
(67, 2, 'Corporate Finance', 17400000), (67, 3, 'Valuation Analyst', 17400000),
(68, 15, 'Talent Management', 16600000), (68, 16, 'Leadership Development', 16600000),
(69, 17, 'Contract Negotiation', 18200000), (69, 18, 'Legal Documentation', 18200000),
(70, 19, 'Brand Strategy', 16400000), (70, 20, 'Advertising Manager', 16400000),
(71, 21, 'Retail Sales', 14200000), (71, 22, 'Sales Trainer', 14200000),
(72, 1, 'FP&A Analyst', 18400000), (72, 4, 'Quality Auditor', 18400000),
(73, 15, 'HR Compliance', 15400000), (73, 16, 'Policy Development', 15400000),
(74, 9, 'Data Governance', 22400000), (74, 11, 'Master Data Management', 22400000),
(75, 12, 'Embedded Systems', 19400000), (75, 13, 'Systems Architect', 19400000),
(76, 10, 'Reinforcement Learning', 24400000), (76, 11, 'Optimization Specialist', 24400000),
(77, 2, 'Investor Relations', 17600000), (77, 3, 'Capital Markets', 17600000),
(78, 15, 'Workforce Planning', 16800000), (78, 16, 'HR Metrics & Analytics', 16800000),
(79, 17, 'Dispute Resolution', 18400000), (79, 18, 'Legal Research', 18400000),
(80, 19, 'Public Relations', 16600000), (80, 20, 'Communications Manager', 16600000),
(81, 21, 'Inside Sales', 14400000), (81, 22, 'Sales Support', 14400000),
(82, 1, 'Financial Systems', 18600000), (82, 4, 'Process Auditor', 18600000),
(83, 15, 'HR Business Analyst', 15600000), (83, 16, 'HR Process Improvement', 15600000),
(84, 9, 'Data Mining Specialist', 22600000), (84, 11, 'Data Warehouse Architect', 22600000),
(85, 12, 'Game Developer', 19600000), (85, 13, 'Creative Director', 19600000),
(86, 10, 'Cognitive Computing', 24600000), (86, 11, 'Decision Science', 24600000),
(87, 2, 'Project Finance', 17800000), (87, 3, 'Structured Finance', 17800000),
(88, 15, 'Compensation Strategy', 17000000), (88, 16, 'Executive Compensation', 17000000),
(89, 17, 'Environmental Law', 18600000), (89, 18, 'Health & Safety Compliance', 18600000),
(90, 19, 'Event Marketing', 16800000), (90, 20, 'Trade Show Manager', 16800000),
(91, 21, 'Sales Administrator', 14600000), (91, 22, 'Order Processing', 14600000),
(92, 1, 'Treasury Management', 18800000), (92, 4, 'Environmental Auditor', 18800000),
(93, 15, 'HR Service Delivery', 15800000), (93, 16, 'HR Shared Services', 15800000),
(94, 9, 'Real-time Analytics', 22800000), (94, 11, 'Stream Processing', 22800000),
(95, 12, 'IoT Developer', 19800000), (95, 13, 'Hardware Engineer', 19800000),
(96, 2, 'Cost Management', 17200000), (96, 3, 'Pricing Analyst', 17200000),
(97, 15, 'HR Strategy', 16000000), (97, 16, 'Organizational Design', 16000000),
(98, 17, 'Privacy Law Specialist', 18800000), (98, 18, 'Data Privacy Officer', 18800000),
(99, 19, 'Digital Strategy', 17000000), (99, 20, 'E-commerce Manager', 17000000),
(100, 21, 'Field Sales', 14800000), (100, 22, 'Regional Manager', 14800000),
(101, 9, 'Data Architect', 23000000), (101, 10, 'Solution Architect', 23000000),
(102, 12, 'QA Lead', 20000000), (102, 13, 'Test Manager', 20000000),
(103, 1, 'Financial Planning', 19000000), (103, 3, 'Investment Manager', 19000000),
(104, 15, 'Learning & Development', 16200000), (104, 16, 'Training Manager', 16200000),
(105, 17, 'Commercial Law', 19000000), (105, 18, 'Contract Manager', 19000000),
(106, 19, 'Marketing Operations', 17200000), (106, 20, 'Marketing Director', 17200000),
(107, 21, 'National Sales', 15000000), (107, 22, 'Sales Director', 15000000),
(108, 9, 'Research Scientist', 23400000), (108, 10, 'AI Ethicist', 23400000),
(109, 12, 'Embedded Engineer', 20200000), (109, 13, 'Firmware Developer', 20200000),
(110, 1, 'Treasury Manager', 19200000), (110, 4, 'Internal Control', 19200000),
(111, 15, 'HR Operations', 16400000), (111, 16, 'HR Service Manager', 16400000),
(112, 17, 'Tax Law Specialist', 19200000), (112, 18, 'Tax Compliance', 19200000),
(113, 19, 'Channel Marketing', 17400000), (113, 20, 'Partner Marketing', 17400000),
(114, 21, 'Strategic Accounts', 15200000), (114, 22, 'Enterprise Sales', 15200000),
(115, 9, 'MLOps Engineer', 23600000), (115, 10, 'Platform Engineer', 23600000),
(116, 12, 'Automation Specialist', 20400000), (116, 13, 'Robotics Engineer', 20400000),
(117, 1, 'Financial Controller', 19400000), (117, 3, 'Risk Manager', 19400000),
(118, 15, 'Talent Acquisition Lead', 16600000), (118, 16, 'Recruitment Director', 16600000),
(119, 17, 'Employment Law', 19400000), (119, 18, 'Labor Relations', 19400000),
(120, 19, 'Product Launch', 17600000), (120, 20, 'Go-to-Market', 17600000),
(121, 21, 'Business Development', 15400000), (121, 22, 'Strategic Partnerships', 15400000),
(122, 9, 'Data Science Lead', 23800000), (122, 10, 'Chief Data Scientist', 23800000),
(123, 12, 'Technical Architect', 20600000), (123, 13, 'Enterprise Architect', 20600000),
(124, 1, 'Chief Financial Officer', 19600000), (124, 3, 'Finance Director', 19600000),
(125, 15, 'Chief HR Officer', 16800000), (125, 16, 'HR Director', 16800000),
(126, 17, 'General Counsel', 19600000), (126, 18, 'Legal Director', 19600000),
(127, 19, 'Chief Marketing Officer', 17800000), (127, 20, 'Marketing VP', 17800000),
(128, 21, 'Chief Sales Officer', 15600000), (128, 22, 'Sales VP', 15600000),
(129, 9, 'VP of Data Science', 24000000), (129, 10, 'Head of AI', 24000000),
(130, 12, 'VP of Engineering', 20800000), (130, 13, 'CTO', 20800000),
(131, 1, 'VP of Finance', 19800000), (131, 4, 'Head of Audit', 19800000),
(132, 15, 'VP of HR', 17000000), (132, 16, 'Head of Talent', 17000000),
(133, 17, 'VP of Legal', 19800000), (133, 18, 'Head of Compliance', 19800000),
(134, 19, 'VP of Marketing', 18000000), (134, 20, 'Head of Brand', 18000000),
(135, 21, 'VP of Sales', 15800000), (135, 22, 'Head of Sales Ops', 15800000),
(136, 9, 'Head of Analytics', 24200000), (136, 10, 'AI Director', 24200000),
(137, 12, 'Engineering Director', 21000000), (137, 13, 'Head of Product', 21000000),
(138, 1, 'Finance Manager', 20000000), (138, 3, 'Head of Treasury', 20000000),
(139, 15, 'HR Director', 17200000), (139, 16, 'Head of HRBP', 17200000),
(140, 17, 'Legal Manager', 20000000), (140, 18, 'Head of Legal Ops', 20000000),
(141, 19, 'Marketing Manager', 18200000), (141, 20, 'Head of Digital', 18200000),
(142, 21, 'Sales Manager', 16000000), (142, 22, 'Head of Channel', 16000000),
(143, 9, 'Analytics Manager', 24400000), (143, 10, 'Head of Research', 24400000),
(144, 12, 'Development Manager', 21200000), (144, 13, 'Head of Dev', 21200000),
(145, 1, 'Accounting Manager', 20200000), (145, 4, 'Head of Reporting', 20200000),
(146, 15, 'Talent Manager', 17400000), (146, 16, 'Head of L&D', 17400000),
(147, 17, 'Compliance Manager', 20200000), (147, 18, 'Head of Risk', 20200000),
(148, 19, 'Campaign Manager', 18400000), (148, 20, 'Head of Media', 18400000),
(149, 21, 'Account Director', 16200000), (149, 22, 'Head of Accounts', 16200000),
(150, 9, 'Data Manager', 24600000), (150, 10, 'Head of ML', 24600000),
(151, 12, 'Project Manager', 21400000), (151, 13, 'Head of Projects', 21400000),
(152, 1, 'Budget Manager', 20400000), (152, 3, 'Head of Budgeting', 20400000),
(153, 15, 'HR Manager', 17600000), (153, 16, 'Head of HR', 17600000),
(154, 17, 'Legal Manager', 20400000), (154, 18, 'Head of Contracts', 20400000),
(155, 19, 'Product Manager', 18600000), (155, 20, 'Head of Products', 18600000),
(156, 21, 'Sales Team Lead', 16400000), (156, 22, 'Head of Sales', 16400000),
(157, 9, 'Tech Lead', 24800000), (157, 10, 'Head of Tech', 24800000),
(158, 12, 'Lead Engineer', 21600000), (158, 13, 'Head of Engineering', 21600000),
(159, 1, 'Lead Analyst', 20600000), (159, 4, 'Head of Analysis', 20600000),
(160, 15, 'Lead HRBP', 17800000), (160, 16, 'Head of People', 17800000);

-- MULTI-TABLE JOIN
SELECT 
    e.EmployeeID,
    e.EmployeeName,
    e.DateOfBirth,
    d.DepartmentName,
    p.ProjectName,
    a.EmployeeRole,
    a.Salary
FROM Employees e
LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID
LEFT JOIN Assignments a ON e.EmployeeID = a.EmployeeID
LEFT JOIN Projects p ON a.ProjectID = p.ProjectID
ORDER BY e.EmployeeID, p.ProjectID;
SELECT * FROM assignments;

