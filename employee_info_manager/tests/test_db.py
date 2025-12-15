"""
Test cases for database operations
"""
import unittest
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from database.connection import DatabaseConnection
from database.models import Employee, Department

class TestDatabase(unittest.TestCase):
    """Test database connection and basic operations"""
    
    @classmethod
    def setUpClass(cls):
        """Set up test database"""
        cls.db = DatabaseConnection(test_mode=True)
        cls.db.connect()
        
        # Create test tables
        with open('database/test_schema.sql', 'r') as f:
            sql = f.read()
            cls.db.execute_query(sql)
    
    def test_connection(self):
        """Test database connection"""
        self.assertTrue(self.db.is_connected())
    
    def test_create_employee(self):
        """Test creating an employee"""
        employee = Employee(
            name="Test Employee",
            date_of_birth="2000-01-01",
            department_id=1
        )
        
        employee_id = self.db.create_employee(employee)
        self.assertIsNotNone(employee_id)
        self.assertGreater(employee_id, 0)
    
    def test_read_employee(self):
        """Test reading employee data"""
        employees = self.db.get_all_employees()
        self.assertIsInstance(employees, list)
    
    @classmethod
    def tearDownClass(cls):
        """Clean up after tests"""
        cls.db.close()

if __name__ == '__main__':
    unittest.main()
