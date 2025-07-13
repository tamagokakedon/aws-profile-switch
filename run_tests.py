#!/usr/bin/env python3
"""
Test runner script for AWS Profile Switch.
This script runs all tests and provides a summary of results.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd, description):
    """Run a command and return the result."""
    print(f"\n{'='*60}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*60}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: Command failed with return code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
        return False


def main():
    """Main test runner function."""
    # Change to the project directory
    project_dir = Path(__file__).parent
    original_dir = Path.cwd()
    
    try:
        import os
        os.chdir(project_dir)
        
        print("AWS Profile Switch - Test Runner")
        print("=" * 60)
        
        # Check if we're in a virtual environment
        venv_info = sys.prefix != sys.base_prefix
        print(f"Virtual environment: {'Yes' if venv_info else 'No'}")
        print(f"Python executable: {sys.executable}")
        print(f"Python version: {sys.version}")
        
        # Install dependencies in development mode
        if not run_command([sys.executable, "-m", "pip", "install", "-e", ".[dev]"], 
                          "Installing package in development mode"):
            print("Failed to install package")
            return False
        
        # Run unit tests
        if not run_command([sys.executable, "-m", "pytest", "tests/", "-v", "--tb=short"], 
                          "Running unit tests"):
            print("Unit tests failed")
            return False
        
        # Run tests with coverage
        if not run_command([sys.executable, "-m", "pytest", "tests/", "--cov=aws_profile_switch", 
                           "--cov-report=term-missing", "--cov-report=html"], 
                          "Running tests with coverage"):
            print("Coverage tests failed")
            return False
        
        # Run type checking with mypy
        if not run_command([sys.executable, "-m", "mypy", "src/aws_profile_switch/"], 
                          "Running type checking"):
            print("Type checking failed")
            return False
        
        # Run code formatting check
        if not run_command([sys.executable, "-m", "black", "--check", "src/", "tests/"], 
                          "Checking code formatting"):
            print("Code formatting check failed")
            return False
        
        # Run linting with flake8
        if not run_command([sys.executable, "-m", "flake8", "src/", "tests/"], 
                          "Running linting"):
            print("Linting failed")
            return False
        
        print("\n" + "=" * 60)
        print("ALL TESTS PASSED! ✅")
        print("=" * 60)
        print("\nProject is ready for use and distribution!")
        print("Coverage report available in htmlcov/index.html")
        
        return True
        
    except Exception as e:
        print(f"Error during test execution: {e}")
        return False
    finally:
        os.chdir(original_dir)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)