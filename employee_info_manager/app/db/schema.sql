-- CREATE DATABASE
DROP DATABASE IF EXISTS Employee_Information_Manager;
CREATE DATABASE Employee_Information_Manager;
USE Employee_Information_Manager;
DELIMITER $$

-- DEPARTMENTS
-- TABLE DEPARTMENTS
CREATE TABLE Departments (
    DepartmentID INT AUTO_INCREMENT PRIMARY KEY,
    DepartmentName VARCHAR(100) UNIQUE NOT NULL
);

-- CREATE DEPARTMENT

CREATE PROCEDURE CreateDepartments(IN p_Name VARCHAR(100))
BEGIN
    INSERT INTO Departments (DepartmentName) VALUES (p_Name);
    SELECT * FROM Departments ORDER BY DepartmentID ASC;
END $$

-- READ DEPARTMENT
-- READ ALL
CREATE PROCEDURE GetDepartments()
BEGIN
    SELECT * FROM Departments ORDER BY DepartmentID ASC;
END $$
-- READ BY ID
CREATE PROCEDURE GetDepartmentsByID(IN p_ID INT)
BEGIN
	SELECT * FROM Departments WHERE DepartmentID = p_ID;
END $$

-- UPDATE DEPARTMENT
CREATE PROCEDURE UpdateDepartment(
    IN p_ID INT,
    IN p_Name VARCHAR(100)
)
BEGIN
    UPDATE Departments SET DepartmentName = p_Name
    WHERE DepartmentID = p_ID;
END$$

-- DELETE DEPARTMENT
CREATE PROCEDURE DeleteDepartment(IN p_ID INT)
BEGIN
    DELETE FROM Departments WHERE DepartmentID = p_ID;
END $$

-- EMPLOYEES
-- TABLE EMPLOYEES
CREATE TABLE Employees (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeName VARCHAR(100) NOT NULL,
    DateOfBirth DATE NOT NULL,
    DepartmentID INT NOT NULL,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);

-- CREATE EMPLOYEES
CREATE PROCEDURE CreateEmployee (
    IN p_Name VARCHAR(100),
    IN p_Birth DATE,
    IN p_DepartmentID INT
)
BEGIN
    INSERT INTO Employees (EmployeeName, DateOfBirth, DepartmentID)
    VALUES (p_Name, p_Birth, p_DepartmentID);
END $$

-- READ EMPLOYEES
-- READ ALL
CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT * FROM Employees;
END;
-- READ BY ID 
CREATE PROCEDURE GetEmployeeByID(IN p_ID INT)
BEGIN
    SELECT * FROM Employees WHERE EmployeeID = p_ID;
END $$

-- UPDATE EMPLOYEES
CREATE PROCEDURE UpdateEmployee (
    IN p_ID INT,
    IN p_Name VARCHAR(100),
    IN p_Birth DATE,
    IN p_DepartmentID INT
)
BEGIN
    UPDATE Employees
    SET EmployeeName = p_Name,
        DateOfBirth = p_Birth,
        DepartmentID = p_DepartmentID
    WHERE EmployeeID = p_ID;
END $$

-- DELETE EMPLOYEES
CREATE PROCEDURE DeleteEmployee(IN p_ID INT)
BEGIN
    DELETE FROM Employees WHERE EmployeeID = p_ID;
END $$

-- PROJECTS
-- TABLE PROJECT
CREATE TABLE Projects (
    ProjectID INT AUTO_INCREMENT PRIMARY KEY,
    ProjectName VARCHAR(100) UNIQUE NOT NULL,
    ManagerEmployeeID INT,
    FOREIGN KEY (ManagerEmployeeID) REFERENCES Employees(EmployeeID)
);

-- CREATE PROJECT
CREATE PROCEDURE CreateProject(
	IN p_Name VARCHAR (100),
    IN p_Manager INT
)
BEGIN 
	INSERT INTO Projects (ProjectName, ManagerEmployeeID)
    VALUES (p_Name, p_Manager);
END $$

-- READ PROJECT
-- READ ALL
CREATE PROCEDURE GetProjects()
BEGIN
    SELECT * FROM Projects;
END $$
-- READ BY ID 
CREATE PROCEDURE GetProjectByID(IN p_ProjectID INT)
BEGIN
    SELECT * FROM Projects 
    WHERE ProjectID = p_ProjectID;
END $$

-- UPDATE PROJECT
CREATE PROCEDURE UpdateProject(
    IN p_ProjectID INT,
    IN p_ProjectName VARCHAR(100),
    IN p_ManagerEmployeeID INT
)
BEGIN
    UPDATE Projects
    SET 
        ProjectName = p_ProjectName,
        ManagerEmployeeID = p_ManagerEmployeeID
    WHERE ProjectID = p_ProjectID;
END $$

-- DELETE PROJECT
CREATE PROCEDURE DeleteProject(IN p_ProjectID INT)
BEGIN
    DELETE FROM Projects
    WHERE ProjectID = p_ProjectID;
END $$

-- ASSIGNMENTS (Employee ↔ Project)
-- TABLE ASSIGNMENTS
CREATE TABLE Assignments (
    AssignmentID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT NOT NULL,
    ProjectID INT NOT NULL,
    EmployeeRole VARCHAR(100) NOT NULL,
    Salary DECIMAL(10,2) NOT NULL CHECK (Salary >= 0),
    UNIQUE(EmployeeID, ProjectID),
    FOREIGN KEY (EmployeeID) REFERENCES Employees(EmployeeID) ON DELETE CASCADE ,
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID) ON DELETE CASCADE
);

-- CREATE ASSIGNMENTS
CREATE PROCEDURE CreateAssignment(
    IN p_EmployeeID INT,
    IN p_ProjectID INT,
    IN p_EmployeeRole VARCHAR(100),
    IN p_Salary DECIMAL(10,2)
)
BEGIN
    INSERT INTO Assignments (EmployeeID, ProjectID, EmployeeRole, Salary)
    VALUES (p_EmployeeID, p_ProjectID, p_EmployeeRole, p_Salary);
END $$

-- READ ASSIGNMENTS
-- READ ALL
CREATE PROCEDURE GetAssignments()
BEGIN
    SELECT * FROM Assignments;
END $$

-- READ BY ID
CREATE PROCEDURE GetAssignmentByID(IN p_AssignmentID INT)
BEGIN
    SELECT * FROM Assignments
    WHERE AssignmentID = p_AssignmentID;
END $$

-- UPDATE ASSIGNMENTS
CREATE PROCEDURE UpdateAssignment(
    IN p_AssignmentID INT,
    IN p_EmployeeID INT,
    IN p_ProjectID INT,
    IN p_EmployeeRole VARCHAR(100),
    IN p_Salary DECIMAL(10,2)
)
BEGIN
    UPDATE Assignments
    SET
        EmployeeID = p_EmployeeID,
        ProjectID = p_ProjectID,
        EmployeeRole = p_EmployeeRole,
        Salary = p_Salary
    WHERE AssignmentID = p_AssignmentID;
END $$

-- DELETE ASSIGNMENTS
CREATE PROCEDURE DeleteAssignment(IN p_AssignmentID INT)
BEGIN
    DELETE FROM Assignments
    WHERE AssignmentID = p_AssignmentID;
END $$

-- JOIN PROCEDURE 
-- INNER JOIN 
DELIMITER $$
CREATE PROCEDURE InnerJoin()
BEGIN
    SELECT 
        e.EmployeeName,
        p.ProjectName,
        a.EmployeeRole,
        a.Salary
    FROM Employees e
    INNER JOIN Assignments a ON e.EmployeeID = a.EmployeeID
    INNER JOIN Projects p ON a.ProjectID = p.ProjectID
    ORDER BY e.EmployeeName, p.ProjectName;
END $$

-- LEFT JOIN

CREATE PROCEDURE LeftJoin()
BEGIN
    SELECT
        e.EmployeeName,
        p.ProjectName,
        a.EmployeeRole,
        a.Salary
    FROM Employees e
    LEFT JOIN Assignments a ON e.EmployeeID = a.EmployeeID
    LEFT JOIN Projects p ON a.ProjectID = p.ProjectID
    ORDER BY e.EmployeeName;
END $$

-- MULTI-TABLE JOIN
DELIMITER $$

CREATE PROCEDURE MultiTableJoin()
BEGIN
    SELECT
        e.EmployeeID,
        e.EmployeeName,
        d.DepartmentName,
        p.ProjectID,
        p.ProjectName,
        a.EmployeeRole,
        a.Salary,
        m.EmployeeName AS ManagerName
    FROM Employees e
    JOIN Departments d 
        ON e.DepartmentID = d.DepartmentID
    JOIN Assignments a 
        ON e.EmployeeID = a.EmployeeID
    JOIN Projects p 
        ON a.ProjectID = p.ProjectID
    LEFT JOIN Employees m 
        ON p.ManagerEmployeeID = m.EmployeeID
    ORDER BY e.EmployeeName, p.ProjectName;
END $$


-- ABOVE AVERAGE SALARY

CREATE PROCEDURE AboveGlobalAverage()
BEGIN
    SELECT 
        e.EmployeeName,
        AVG(a.Salary) AS AvgSalary
    FROM Employees e
    JOIN Assignments a ON e.EmployeeID = a.EmployeeID
    GROUP BY e.EmployeeID
    HAVING AVG(a.Salary) > (
        SELECT AVG(Salary) FROM Assignments
    )
    ORDER BY AvgSalary DESC;
END $$

-- SEARCH AND FILTER 
-- NHỮNG BIẾN ĐƯỢC NHẬP VÀO
CREATE PROCEDURE SearchAndFilter(
    IN p_keyword VARCHAR(255),
    IN p_departmentName VARCHAR(255),
    IN p_projectName VARCHAR(255),
    IN p_role VARCHAR(255),
    IN p_salaryMin INT,
    IN p_salaryMax INT,
    IN p_managerName VARCHAR(255)
)
BEGIN
-- GHÉP BẢNG NHÉ
    SELECT 
        e.EmployeeID,
        e.EmployeeName,
        d.DepartmentName,
        p.ProjectName,
        a.EmployeeRole,
        a.Salary,
        m.EmployeeName AS ManagerName
    FROM Employees e
    LEFT JOIN Assignments a ON e.EmployeeID = a.EmployeeID
    LEFT JOIN Projects p ON a.ProjectID = p.ProjectID
    LEFT JOIN Employees m ON p.ManagerEmployeeID = m.EmployeeID
    LEFT JOIN Departments d ON e.DepartmentID = d.DepartmentID
    WHERE 
    -- TÌM THEO KÍ TỰ GẦN GIỐNG CHỨ KHÔNG PHẢI TÌM CHÍNH XÁC MỘT CÁI TÊN
        e.EmployeeName LIKE CONCAT('%', p_keyword, '%')
    -- ÁP THÊM ĐIỀU KIỆN UwU
        AND (p_departmentName IS NULL OR d.DepartmentName LIKE CONCAT('%', p_departmentName, '%'))
        AND (p_projectName IS NULL OR p.ProjectName LIKE CONCAT('%', p_projectName, '%'))
        AND (p_role IS NULL OR a.EmployeeRole LIKE CONCAT('%', p_role, '%'))
        AND (p_salaryMin IS NULL OR a.Salary >= p_salaryMin) -- LƯƠNG GIỚI HẠN TRÁI (NHỎ NHẤT LÀ)
        AND (p_salaryMax IS NULL OR a.Salary <= p_salaryMax) -- LƯƠNG GIỚI HẠN PHẢI (LỚN NHẤT LÀ)
        AND (p_managerName IS NULL OR m.EmployeeName LIKE CONCAT('%', p_managerName, '%'));
END $$
 




