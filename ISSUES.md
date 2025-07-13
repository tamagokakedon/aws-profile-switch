# Implementation Issues and Tasks

This document outlines the decomposed implementation tasks for the `aws-profile-switch` tool.

## High Priority Issues

### Issue #1: Project Structure Setup
**Status**: Pending  
**Priority**: High  
**Description**: Set up the basic Python project structure with proper packaging configuration.

**Tasks**:
- Create `pyproject.toml` with project metadata and dependencies
- Set up package directory structure (`src/aws_profile_switch/`)
- Configure entry point for CLI command
- Add initial `__init__.py` files

**Dependencies**: None  
**Estimated Effort**: 1-2 hours

### Issue #2: AWS Config File Parser
**Status**: Pending  
**Priority**: High  
**Description**: Implement functionality to read and parse AWS CLI configuration files.

**Tasks**:
- Create parser module using Python's `configparser`
- Read `~/.aws/config` file
- Extract profile sections and their properties
- Handle file not found and parsing errors gracefully

**Dependencies**: None  
**Estimated Effort**: 2-3 hours

### Issue #3: SSO Profile Data Structure
**Status**: Pending  
**Priority**: High  
**Description**: Define data structures to store and manage SSO profile information.

**Tasks**:
- Create `SSOProfile` dataclass/model
- Include fields: `profile_name`, `sso_account_name`, `sso_account_id`, `sso_role_name`, `sso_start_url`
- Implement validation and serialization methods
- Create profile collection/manager class

**Dependencies**: Issue #2  
**Estimated Effort**: 2-3 hours

### Issue #4: SSO Profile Identification
**Status**: Pending  
**Priority**: High  
**Description**: Implement logic to identify and filter SSO-related profiles from AWS config.

**Tasks**:
- Check for `sso_auto_populated = true` flag
- Validate presence of required SSO fields
- Filter out non-SSO profiles
- Handle edge cases and malformed profiles

**Dependencies**: Issue #2, Issue #3  
**Estimated Effort**: 2-3 hours

### Issue #5: Prompt Toolkit UI Framework
**Status**: Pending  
**Priority**: High  
**Description**: Set up the interactive UI framework using `prompt_toolkit`.

**Tasks**:
- Initialize `prompt_toolkit` application
- Create basic candidate list display
- Implement text input handling
- Set up event loop and application structure

**Dependencies**: None  
**Estimated Effort**: 3-4 hours

## Medium Priority Issues

### Issue #6: Keyboard Navigation
**Status**: Pending  
**Priority**: Medium  
**Description**: Implement keyboard input handling for UI navigation.

**Tasks**:
- Bind arrow keys for candidate navigation
- Implement Enter key for selection confirmation
- Add Esc key for cancellation
- Handle special keys (Tab, Backspace, etc.)

**Dependencies**: Issue #5  
**Estimated Effort**: 2-3 hours

### Issue #7: History Management
**Status**: Pending  
**Priority**: Medium  
**Description**: Create system to track and display recently used profiles.

**Tasks**:
- Implement JSON-based history storage in user home directory
- Track profile usage with timestamps
- Display 5 most recent profiles on startup
- Handle history file corruption gracefully

**Dependencies**: Issue #3  
**Estimated Effort**: 2-3 hours

### Issue #8: Fuzzy Search Algorithm
**Status**: Pending  
**Priority**: Medium  
**Description**: Implement fuzzy search for account and role names.

**Tasks**:
- Create fuzzy matching algorithm (or use library like `fuzzywuzzy`)
- Search across `sso_account_name` and `sso_role_name` fields
- Implement real-time search result updates
- Optimize for performance with large profile lists

**Dependencies**: Issue #3  
**Estimated Effort**: 3-4 hours

### Issue #9: Multi-Stage Profile Selection
**Status**: Pending  
**Priority**: Medium  
**Description**: Build the progressive filtering workflow for profile selection.

**Tasks**:
- Implement state management for selection stages
- Create account name selection phase
- Create role name selection phase
- Handle transitions between stages
- Format display information appropriately for each stage

**Dependencies**: Issue #5, Issue #6, Issue #8  
**Estimated Effort**: 4-5 hours

### Issue #10: Shell Environment Detection
**Status**: Pending  
**Priority**: Medium  
**Description**: Detect shell environment and output appropriate commands.

**Tasks**:
- Detect Bash/Zsh vs PowerShell environments
- Generate `export AWS_PROFILE="<profile>"` for Unix shells
- Generate `$env:AWS_PROFILE = "<profile>"` for PowerShell
- Handle edge cases and unknown shells

**Dependencies**: Issue #9  
**Estimated Effort**: 2-3 hours

### Issue #11: Error Handling
**Status**: Pending  
**Priority**: Medium  
**Description**: Add comprehensive error handling and user-friendly messages.

**Tasks**:
- Handle missing `~/.aws/config` file
- Gracefully handle parsing errors
- Provide clear error messages for common issues
- Implement logging for debugging
- Add validation for all user inputs

**Dependencies**: All core functionality issues  
**Estimated Effort**: 3-4 hours

### Issue #12: Unit Tests
**Status**: Pending  
**Priority**: Medium  
**Description**: Create comprehensive unit tests for all core functionality.

**Tasks**:
- Set up pytest framework
- Create test fixtures for AWS config files
- Test profile parsing and identification
- Test fuzzy search functionality
- Test UI components where possible
- Achieve >90% code coverage

**Dependencies**: All core functionality issues  
**Estimated Effort**: 4-6 hours

## Low Priority Issues

### Issue #13: Integration Tests
**Status**: Pending  
**Priority**: Low  
**Description**: Create end-to-end integration tests for the complete workflow.

**Tasks**:
- Create test scenarios with mock AWS config files
- Test complete profile selection workflow
- Test shell command output
- Test error scenarios
- Performance testing with large profile lists

**Dependencies**: Issue #12  
**Estimated Effort**: 3-4 hours

---

## Implementation Order

1. **Phase 1**: Issues #1-4 (Core functionality)
2. **Phase 2**: Issues #5-6 (Basic UI)  
3. **Phase 3**: Issues #7-10 (Advanced features)
4. **Phase 4**: Issues #11-12 (Polish and testing)
5. **Phase 5**: Issue #13 (Integration testing)

## Testing Strategy

- Unit tests for each module using pytest
- Mock AWS config files for testing
- Test both positive and negative scenarios
- Performance testing with large datasets
- Manual testing on different platforms (Linux, WSL, Windows)