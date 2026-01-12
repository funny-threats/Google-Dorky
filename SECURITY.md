# Security Policy

## Supported Versions

We release patches for security vulnerabilities. Which versions are eligible for receiving such patches depends on the CVSS v3.0 Rating:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities privately to maintainers rather than using public issue trackers.

**Do NOT create a public GitHub issue for security vulnerabilities.**

Instead, please email security concerns to: [your-email@example.com]

Include the following information:
- Type of vulnerability
- Full paths of source file(s) related to the vulnerability
- Location of the affected code (tag/branch/commit or direct URL)
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit the issue

## Security Best Practices

When using this tool:

1. **Only use on authorized systems** - Never use this tool on systems you don't own or have explicit permission to test
2. **Keep dependencies updated** - Regularly update dependencies to patch known vulnerabilities
3. **Use virtual environments** - Isolate the tool's dependencies from your system Python
4. **Review code** - Review the source code before running, especially if downloading from untrusted sources
5. **Monitor network traffic** - Be aware of what network connections the tool makes
6. **Protect your results** - Keep scan results secure and don't share sensitive findings publicly

## Responsible Disclosure

We follow responsible disclosure practices:

- We will acknowledge receipt of your vulnerability report within 48 hours
- We will provide an initial assessment within 7 days
- We will keep you informed of our progress
- We will notify you when the vulnerability is fixed
- We will credit you in the release notes (unless you prefer to remain anonymous)

## Known Limitations

This tool is provided as-is for educational and authorized testing purposes. Users should be aware that:

- Free proxies may be unreliable or malicious
- Google may rate limit or block automated searches
- SQL injection detection may produce false positives/negatives
- Always manually verify findings before reporting

## Disclaimer

The authors and contributors are not responsible for any misuse of this tool. Users are solely responsible for ensuring they have proper authorization before testing any systems.
