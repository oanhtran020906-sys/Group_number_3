"""
Test cases for business logic services
"""
import unittest
import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from services.employee_service import EmployeeService
from services.department_service import DepartmentService

class TestEmployeeService(unittest.TestCase):
    """Test employee service"""
    
    def setUp(self):
        self.employee_service = EmployeeService()
    
    def test_validate_employee_data(self):
        """Test employee data validation"""
        # Test valid data
        valid_data = {
            'name': 'John Doe',
            'date_of_birth': '1990-01-01',
            'department_id': 1
        }
        self.assertTrue(self.employee_service.validate_data(valid_data))
        
        # Test invalid data - empty name
        invalid_data = {
            'name': '',
            'date_of_birth': '1990-01-01',
            'department_id': 1
        }
        self.assertFalse(self.employee_service.validate_data(invalid_data))
    
    def test_calculate_age(self):
        """Test age calculation"""
        from datetime import datetime
        
        # Mock current date
        current_year = datetime.now().year
        birth_year = 1990
        expected_age = current_year - birth_year
        
        age = self.employee_service.calculate_age(f"{birth_year}-01-01")
        self.assertEqual(age, expected_age)

class TestDepartmentService(unittest.TestCase):
    """Test department service"""
    
    def setUp(self):
        self.dept_service = DepartmentService()
    
    def test_department_exists(self):
        """Test department existence check"""
        # This would test if department exists in database
        # Mock database call for test
        pass

if __name__ == '__main__':
    unittest.main()
