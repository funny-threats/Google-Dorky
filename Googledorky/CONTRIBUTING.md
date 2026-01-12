# Contributing to Google Dork SQL Injection Scanner

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing to this project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow

## How to Contribute

### Reporting Issues

1. Check if the issue already exists
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, Python version)

### Suggesting Features

1. Open an issue with the `enhancement` label
2. Describe the feature and its use case
3. Discuss implementation approach

### Pull Requests

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Follow code style guidelines
5. Test your changes
6. Commit with clear messages (`git commit -m 'Add amazing feature'`)
7. Push to your branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/Googledorky.git
cd Googledorky

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Make changes and test
python main.py --dorks dorks.txt
```

## Code Style

- Follow PEP 8 style guide
- Use meaningful variable names
- Add comments for complex logic
- Keep functions focused and small
- Write docstrings for functions and classes

## Testing

Before submitting:
- Test with different dork files
- Verify proxy functionality
- Check error handling
- Ensure no breaking changes

## Areas for Contribution

- Additional proxy sources
- Improved SQL injection detection
- Enhanced database parsing
- Better error handling
- Performance optimizations
- Documentation improvements
- Additional Google dorks

## Questions?

Open an issue with the `question` label for any questions or clarifications.

Thank you for contributing! 🎉
