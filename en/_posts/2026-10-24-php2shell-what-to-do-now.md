---
layout: single
title: "PHP2Shell: what to do now (CVE-2026-109618 and CVE-2026-109619)"
date: 2026-10-24
permalink: /en/blog/vulnerabilities/php2shell-what-to-do-now/
excerpt: "Two critical PHP flaws, found with the help of AI. Fixed versions, what to check and what to do right away."
seo_title: "PHP2Shell: what to do now (CVE-2026-109618 and CVE-2026-109619)"
seo_description: "PHP2Shell: fixed PHP versions, how to check your site and what to do right away, explained simply."
categories:
  - Vulnerabilities
header:
  teaser: /assets/images/blog/php2shell-cosa-e-successo.svg
  image: /assets/images/blog/php2shell-cosa-e-successo.svg
ref: php2shell
lang: en
locale: en
tr: tradotto
tr_hash: i0fpe2
---

Wiz researchers explained that flaws present for decades were hard to turn into an attack, but the most advanced AI models have lowered that barrier. That is why patching quickly matters more than before.

On 21 October 2026 the PHP security team released emergency updates for two critical vulnerabilities, **CVE-2026-109618** and **CVE-2026-109619**, nicknamed PHP2Shell. Both score 9.2 out of 10 on CVSS v4.0 and, with specially crafted web requests, can allow code execution on the server without authentication. The greatest risk concerns setups with Apache and mod_php. The flaws are in the PHP interpreter, not in a single CMS: WordPress, Joomla and custom applications are exposed too if they run on a vulnerable version.

## Fixed versions

| PHP branch | Fixed version |
|---|---|
| 8.5 | 8.5.12 |
| 8.4 | 8.4.27 |
| 8.3 | 8.3.36 |
| 8.2 | 8.2.35 |

The 8.2 branch will not receive fixes after 31 December 2026. If you run a branch older than those listed, it is no longer supported and must be moved to one that is.

## What to do right now

1. **Check the version.** From a terminal: `php -v`. On shared hosting: control panel, "PHP version" section. Note that the command line can show a different version from the one your site uses.
2. **Update** to a fixed version through your operating system, package or hosting provider, then restart the web service.
3. **If you cannot update right away**, temporary measures reduce exposure but do not remove it. For example, disabling `session.upload_progress.enabled` blocks only one demonstrated path for CVE-2026-109619 and does not protect against CVE-2026-109618. A web application firewall (WAF) can buy time. The real fix is updating.
4. **Check for compromise**: new or recently modified PHP files, unusual access, odd requests in the logs. For internet-facing servers that were not updated in recent days, it is prudent to also rotate passwords and keys.
5. **Verify your backup**: that it exists, is recent and can be restored.

## Do you have managed hosting?
Some providers have already updated the servers they manage. Ask for written confirmation of the version in use. The problem remains for VPS, unmanaged hosting and applications that were never updated.

## Want us to do it?
Verification, update, compromise check, password and key rotation, verified backup: see our [services]({{ '/en/services/' | relative_url }}) or [contact us]({{ '/en/contact/' | relative_url }}).

## Sources
- [Official PHP security advisory](https://www.php.net/archive/2026.php#2026-10-21-5)
- [Help Net Security: PHP2Shell, update now](https://helpnetsecurity.com/2026/10/21/php2shell-php-vulnerabilities-patched-cve-2026-109618-cve-2026-109619)
- [Tanium: responding to CVE-2026-109618 and CVE-2026-109619](https://www.tanium.com/blog/php2shell-responding-to-cve-2026-109618-and-cve-2026-109619)
