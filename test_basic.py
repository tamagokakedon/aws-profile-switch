#!/usr/bin/env python3
"""
Basic test to verify aws-profile-switch can parse AWS config.
"""

from aws_profile_switch.core import AWSProfileSwitcher


def test_basic_functionality():
    """Test basic functionality without UI."""
    try:
        switcher = AWSProfileSwitcher()
        
        # Test profile listing
        profiles = switcher.list_profiles()
        print(f"Found {len(profiles)} SSO profiles:")
        
        for profile in profiles:
            print(f"  - {profile['profile_name']}: {profile['display_name']}")
        
        # Test shell command generation
        if profiles:
            profile_name = profiles[0]['profile_name']
            command = switcher.get_shell_command(profile_name)
            print(f"\nShell command for '{profile_name}':")
            print(f"  {command}")
        
        print("\n✅ Basic functionality works!")
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    test_basic_functionality()