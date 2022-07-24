###### Scrape the latest Google News propaganda!

###### Be sure to run multiple times per day as propaganda changes quickly!


Retrieves Google News links using Selenium Webdriver. Each article's link, title, and OG Image
are scraped. All results are output to a text file as serialized JSON.

This script is great if you need to add a news feed to your webapp/website with OG preview images.

Tested with Chrome v103; provide absolute or relative path to the chromedriver binary
(I prefer to keep it in project root).

Example usage:
<pre>
    <code>
# Run with visible browser
python boogle.py -p chromedriver.exe

# Run headless in terminal only:
python boogle.py -p chromedriver.exe -x
    </code>
</pre>

Requirements:
Python3, selenium, requests

The results will be written to the current working directory.
Each section will have a list of dictionaries in order from newest to oldest.

<pre>
    <code>
# Extremely Shortened example (there will typically be hundreds of articles):
{
    "US": [
        {
            "title": "Suspected attacker of GOP Rep. Lee Zeldin arrested on federal assault charge",
            "link": "https://news.google.com/articles/CBMiY2h0dHBzOi8vd3d3LmNubi5jb20vMjAyMi8wNy8yMy9wb2xpdGljcy96ZWxkaW4tc3VzcGVjdGVkLWF0dGFja2VyLWZlZGVyYWwtYXNzYXVsdC1jaGFyZ2UvaW5kZXguaHRtbNIBZ2h0dHBzOi8vYW1wLmNubi5jb20vY25uLzIwMjIvMDcvMjMvcG9saXRpY3MvemVsZGluLXN1c3BlY3RlZC1hdHRhY2tlci1mZWRlcmFsLWFzc2F1bHQtY2hhcmdlL2luZGV4Lmh0bWw?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        },
        {
            "title": "Lee Zeldin attack suspect arrested on federal assault charge",
            "link": "https://news.google.com/articles/CAIiEKCr8RKbYDpYiqoebBCOaiAqGQgEKhAIACoHCAowwL2ICzCckocDMMaPqQY?uo=CAUiVWh0dHBzOi8vd3d3LmZveG5ld3MuY29tL3BvbGl0aWNzL2xlZS16ZWxkaW4tYXR0YWNrLXN1c3BlY3QtaGl0LWZlZGVyYWwtYXNzYXVsdC1jaGFyZ2XSAQA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/4pEYXUr42ktGAJvwboyRsDd-rZmaXQTkmX9Y4Ku5M3MyGH1dbJOIzZzFGJ12lvgGc8TyJMBkYsITqIoBUuk=rj-w512-h512-pf"
        },
        {
            "title": "Pilot seriously injured in small plane crash near San Jose's Reid-Hillview Airport",
            "link": "https://news.google.com/articles/CCAiC3dKek1GSmd6SjlNmAEB?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        }
    ],
    "World": [
        {
            "title": "Russian missiles hit Ukraine port; Kyiv says it is still preparing grain exports",
            "link": "https://news.google.com/articles/CBMiaWh0dHBzOi8vd3d3LnJldXRlcnMuY29tL3dvcmxkL2V1cm9wZS91cy1wbGVkZ2VzLW1vcmUtbWlsaXRhcnktYWlkLXVrcmFpbmUtcGVhY2Utc2VlbXMtZmFyLW9mZi0yMDIyLTA3LTIyL9IBAA?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        },
        {
            "title": "Russian missiles strike Odesa one day after grain export deal agreed",
            "link": "https://news.google.com/articles/CBMiX2h0dHBzOi8vd3d3LmNubi5jb20vMjAyMi8wNy8yMy9ldXJvcGUvcnVzc2lhLXVrcmFpbmUtb2Rlc2Etc3RyaWtlLWdyYWluLWV4cG9ydHMtaW50bC9pbmRleC5odG1s0gFjaHR0cHM6Ly9hbXAuY25uLmNvbS9jbm4vMjAyMi8wNy8yMy9ldXJvcGUvcnVzc2lhLXVrcmFpbmUtb2Rlc2Etc3RyaWtlLWdyYWluLWV4cG9ydHMtaW50bC9pbmRleC5odG1s?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        },
        {
            "title": "Damascus air base, Iranian warehouse said hit in alleged Israeli strikes",
            "link": "https://news.google.com/articles/CBMicGh0dHBzOi8vd3d3LnRpbWVzb2Zpc3JhZWwuY29tL2RhbWFzY3VzLWFpci1iYXNlLWlyYW5pYW4td2FyZWhvdXNlLXNhaWQtaGl0LWluLWFsbGVnZWQtaXNyYWVsaS1zdHJpa2VzLW92ZXJuaWdodC_SAXRodHRwczovL3d3dy50aW1lc29maXNyYWVsLmNvbS9kYW1hc2N1cy1haXItYmFzZS1pcmFuaWFuLXdhcmVob3VzZS1zYWlkLWhpdC1pbi1hbGxlZ2VkLWlzcmFlbGktc3RyaWtlcy1vdmVybmlnaHQvYW1wLw?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        }
    ],
    "Business": [
        {
            "title": "'Ruffling feathers': How VW fell out of love with Herbert Diess",
            "link": "https://news.google.com/articles/CAIiEPbA3AzxiVMNmjLxxuwTMEYqGAgEKg8IACoHCAow-4fWBzD4z0gw_fCpBg?uo=CAUiP2h0dHBzOi8vd3d3LmZ0LmNvbS9jb250ZW50L2RlMzg1OGYyLTEyNGMtNDc4YS04ZmFkLTg1NDAxMzVhNDI5NtIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/MgdbXy28m7SBis1XkBT2HZA8rlekakSGEh3ZKS5A74_pKB5i0OPv-LOv4Ww8Yo38I-bwI8J3ln7U08UY6A=rj-w512-h512-pf"
        },
        {
            "title": "JPMorgan's Michele Says Bonds Have Recession 'Priced In'",
            "link": "https://news.google.com/articles/CAIiEG4cw78QqT8sWDx22mofcbYqGQgEKhAIACoHCAow4uzwCjCF3bsCMIrOrwM?uo=CAUiaWh0dHBzOi8vd3d3LmJsb29tYmVyZy5jb20vbmV3cy9hcnRpY2xlcy8yMDIyLTA3LTIzL2pwbW9yZ2FuLXMtbWljaGVsZS1zYXlzLWJvbmRzLWhhdmUtcmVjZXNzaW9uLXByaWNlZC1pbtIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/L-vg-zfNDdJaisw2o_BGJVAgPz0Z1vBq26fy-UDDN-idngSpUVktjfpqxWWxqyWSsdNbZ3O4Lfnp0mxFXoA=rj-w512-h512-pf"
        },
        {
            "title": "U.S. housing affordability poised to fall to lowest since GFC on soaring prices, rates",
            "link": "https://news.google.com/articles/CAIiEL_vXuNibpbvjdHFCEvX0IsqFggEKg0IACoGCAowkqEGMJBZMMTouwY?uo=CAUieWh0dHBzOi8vc2Vla2luZ2FscGhhLmNvbS9uZXdzLzM4NTk3NTQtdXMtaG91c2luZy1hZmZvcmRhYmlsaXR5LXBvaXNlZC10by1mYWxsLXRvLWxvd2VzdC1zaW5jZS1nZmMtb24tc29hcmluZy1wcmljZXMtcmF0ZXPSAQA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/2A9_np-zzhkr_UmtF6q-d-NG3YFZhiYMzZpyIzgm13f8xTvavO63t4kCTbzq8NC2RyWynzrL3E7UHY_NpRJL=rj-w512-h512-pf"
        }
    ],
    "Technology": [
        {
            "title": "Preorder Google's Pixel 6A and get a free set of Pixel Buds A-Series earbuds",
            "link": "https://news.google.com/articles/CAIiEJZ7lp5DVWN_4e5zGdQdTL8qFwgEKg4IACoGCAow3O8nMMqOBjCkztQD?uo=CAUijAFodHRwczovL3d3dy50aGV2ZXJnZS5jb20vZ29vZC1kZWFscy8yMDIyLzcvMjMvMjMyNzM5MzkvZ29vZ2xlLXBpeGVsLTZhLWJ1ZHMtcHJvLWEtc2VyaWVzLW5pbnRlbmRvLXN3aXRjaC1saXRlLWxlbm92by1nYW1pbmctbGFwdG9wLWRlYWwtc2FsZdIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/jWgoOLT4dcvYUm9LKVaLsBOKeh3C0V07ptarOwXpBE9orLUBtCvUPK37EZvW6l5FIy10wqcwbdepQl5PZVQ=rj-w512-h512-pf"
        },
        {
            "title": "Pixel 6a Review: Value-packed, Tensor-powered, and just in time for Pixel 3a upgrades",
            "link": "https://news.google.com/articles/CAIiELSloigPgHSaEcwQM3v51QUqGQgEKhAIACoHCAowyoD5CjD5z-ACMM_rvwU?uo=CAUiANIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/ZRA2q5_IkzSRsbLulooiJZvAlIHBkwXP1zTaVFAZcV1Lye8lmGqKh-RCdLXXPYl9gugpuT4h0ORXLZfgLA=rj-w512-h512-pf"
        },
        {
            "title": "iPhone 13 camera before iPhone 14 launch: Apple and Android keep failing to make real camera phones",
            "link": "https://news.google.com/articles/CBMiiwFodHRwczovL3d3dy5waG9uZWFyZW5hLmNvbS9uZXdzL2lwaG9uZS0xMy1jYW1lcmEtYmVmb3JlLWlwaG9uZS0xNC1sYXVuY2gtYXBwbGUtYW5kLWFuZHJvaWQta2VlcC1mYWlsaW5nLXRvLW1ha2UtcmVhbC1jYW1lcmEtcGhvbmVzX2lkMTQxNDE50gEA?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        }
    ],
    "Entertainment": [
        {
            "title": "Star Trek teases Picard cast and Strange New Worlds crossover",
            "link": "https://news.google.com/articles/CAIiENQ5A2DcIcz8jita-pMfwIQqFwgEKg4IACoGCAow3O8nMMqOBjCzr7gD?uo=CAUiiwFodHRwczovL3d3dy50aGV2ZXJnZS5jb20vMjAyMi83LzIzLzIzMjc1NDQ0L3N0YXItdHJlay1waWNhcmQtY2FzdC1zdHJhbmdlLW5ldy13b3JsZC1jcm9zc292ZXItdHJhaWxlci10ZWFzZXItcGFyYW1vdW50LXBsdXMtcGF0cmljay1zdGV3YXJ00gEA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/UbQAZlUZvtL0r-qoeUX-uyrLwlq2A4G08xmN6HcqWUfjYXSmezMYEf80Lm0cDLDEyWkq_OLIHmJSEo7N2-Kr=rj-w512-h512-pf"
        },
        {
            "title": "Ben Affleck Appears to Take a Nap on Boat Ride During Post-Wedding Trip With Jennifer Lopez",
            "link": "https://news.google.com/articles/CAIiEOfeMhcjGFVLqNywaooBReAqGQgEKhAIACoHCAowq_7zCjCt4tQCMPa0pwY?uo=CAUiANIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/eFpTNxOtwzAtmXYsuB6p2GhhKK7L2wk7_ykA_0kiNbuFuMiZxd3ogzN2h8VMyDXh1kLc-FMQ6PhONuxXObsT=rj-w512-h512-pf"
        },
        {
            "title": "Zac Efron returns to the school where he filmed hit High School Musical series",
            "link": "https://news.google.com/articles/CAIiEDk9SpCKbqfm_6DnpDaLAHgqGQgEKhAIACoHCAowzuOICzCZ4ocDMNTCoAY?uo=CAUiANIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/WLvIShgfOhVMTmaFSfZqcNhzyxWpZjWZ6i2SBH8ukbrWKLSIH5xfL2T14lWwLpqPGMtD384m1l4-HQ7JXiA=rj-w512-h512-pf"
        }
    ],
    "Sports": [
        {
            "title": "Curtis Blaydes Octagon Interview | UFC London",
            "link": "https://news.google.com/articles/CCAiCzZYajVjYnV2WkFNmAEB?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        },
        {
            "title": "What time does UFC London start for UK fans and what\u2019s the fight order?",
            "link": "https://news.google.com/articles/CAIiEJs_toOlsOy1Ad3cwhLyuRUqGQgEKhAIACoHCAow8KiRCzCh9qUDMI2c1gY?uo=CAUibGh0dHBzOi8vd3d3LmhpdGMuY29tL2VuLWdiLzIwMjIvMDcvMjMvd2hhdC10aW1lLWRvZXMtdWZjLWxvbmRvbi1zdGFydC1mb3ItdWstZmFucy1hbmQtd2hhdHMtdGhlLWZpZ2h0LW9yZGVyL9IBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/3IRXilz-DhN2B7q51GOsP3Hd5tEUbwm5Xn3ct8PU8DTwPNOJ_tmUKWER0mWfjzWFjKBmvsnfw0GXd76ZtkU=rj-w512-h512-pf"
        },
        {
            "title": "Colorado Springs thrower Kara Winger earns first javelin medal for U.S. at world championships",
            "link": "https://news.google.com/articles/CBMiqgFodHRwczovL2dhemV0dGUuY29tL3Nwb3J0cy9jb2xvcmFkby1zcHJpbmdzLXRocm93ZXIta2FyYS13aW5nZXItZWFybnMtZmlyc3QtamF2ZWxpbi1tZWRhbC1mb3ItdS1zLWF0LXdvcmxkLWNoYW1waW9uc2hpcHMvYXJ0aWNsZV8zZDYzZTU4Mi0wYWEzLTExZWQtOWJhZC05N2IyMDRjY2M5OWEuaHRtbNIBrgFodHRwczovL2dhemV0dGUuY29tL3Nwb3J0cy9jb2xvcmFkby1zcHJpbmdzLXRocm93ZXIta2FyYS13aW5nZXItZWFybnMtZmlyc3QtamF2ZWxpbi1tZWRhbC1mb3ItdS1zLWF0LXdvcmxkLWNoYW1waW9uc2hpcHMvYXJ0aWNsZV8zZDYzZTU4Mi0wYWEzLTExZWQtOWJhZC05N2IyMDRjY2M5OWEuYW1wLmh0bWw?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        }
    ],
    "Science": [
        {
            "title": "Watch a SpaceX Falcon 9 rocket soar over the moon in incredible tracking cam video",
            "link": "https://news.google.com/articles/CAIiEIbvlv5pWdaVDnfijSqI9KIqMwgEKioIACIQiaYKTaVj4jekEifjHCx8jCoUCAoiEImmCk2lY-I3pBIn4xwsfIww37rKBg?uo=CAUiQmh0dHBzOi8vd3d3LnNwYWNlLmNvbS9zcGFjZXgtZmFsY29uLTktbW9vbi1mb290YWdlLXN0YXJsaW5rLWxhdW5jaNIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/HO2appXsHjcpL7TVCo57YBlB3FjbouVkrZamFj5ehsUtZz2LVN9d14Uzq8LLaRiYPgp5RBKePpEGeq6cALw0=rj-w512-h512-pf"
        },
        {
            "title": "Laser Marking on Mars - NASA Mars",
            "link": "https://news.google.com/articles/CBMiSGh0dHBzOi8vbWFycy5uYXNhLmdvdi9tYXJzMjAyMC9taXNzaW9uL3N0YXR1cy8zOTMvbGFzZXItbWFya2luZy1vbi1tYXJzL9IBAA?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        },
        {
            "title": "Rocket Report: A heavy-lift rocket funded by crypto; Falcon 9 damaged in transport",
            "link": "https://news.google.com/articles/CBMieWh0dHBzOi8vYXJzdGVjaG5pY2EuY29tL3NjaWVuY2UvMjAyMi8wNy9yb2NrZXQtcmVwb3J0LWEtaGVhdnktbGlmdC1yb2NrZXQtZnVuZGVkLWJ5LWNyeXB0by1mYWxjb24tOS1kYW1hZ2VkLWluLXRyYW5zcG9ydC_SAX9odHRwczovL2Fyc3RlY2huaWNhLmNvbS9zY2llbmNlLzIwMjIvMDcvcm9ja2V0LXJlcG9ydC1hLWhlYXZ5LWxpZnQtcm9ja2V0LWZ1bmRlZC1ieS1jcnlwdG8tZmFsY29uLTktZGFtYWdlZC1pbi10cmFuc3BvcnQvP2FtcD0x?hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/J6_coFbogxhRI9iM864NL_liGXvsQp2AupsKei7z0cNNfDvGUmWUy20nuUhkREQyrpY4bEeIBuc=s0-w300"
        }
    ],
    "Health": [
        {
            "title": "WHO Declares Monkeypox a Global Health Emergency",
            "link": "https://news.google.com/articles/CAIiEJgUhIQ9PkQuzuSdNObiHqcqGAgEKg8IACoHCAow1tzJATDnyxUwxMrPBg?uo=CAUiANIBAA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/7ZuQlaytBtlkaBkhWEv9GeZhll3A6Mq16Dkeo8qkCrMX_jq5awnrKm9lKQ0RIxbF3DO-8zhiQMcA9Z7H_Q=rj-w512-h512-pf"
        },
        {
            "title": "Monkeypox: What to Know About Vaccines, Tests and Treatment",
            "link": "https://news.google.com/articles/CAIiEEBSTvIrx_ZLPsbd2jW4f6AqFwgEKg8IACoHCAowjuuKAzCWrzwwt4QY?uo=CAUiTWh0dHBzOi8vd3d3Lm55dGltZXMuY29tLzIwMjIvMDcvMjEvd2VsbC9saXZlL21vbmtleXBveC12YWNjaW5lLXRyZWF0bWVudC5odG1s0gEA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/l0yDgf7l3yXgF_ju38UlnTWObsZ8gaOeY81aS57h9rpad71QifHZovC9tSPiWhGcJgWQSZupQlp7ogmGrg=rj-w512-h512-pf"
        },
        {
            "title": "Self-Reflection Linked to Improved Late-Life Cognition and Brain Health",
            "link": "https://news.google.com/articles/CAIiEM5ZQJ9rfz8bFMO23QEGJrEqGQgEKhAIACoHCAow_e2PCzDGtqMDMNbzsAY?uo=CAUiQ2h0dHBzOi8vbmV1cm9zY2llbmNlbmV3cy5jb20vc2VsZi1yZWZsZWN0aW9uLWFnaW5nLWNvZ25pdGlvbi0yMTA5OS_SAQA&hl=en-US&gl=US&ceid=US%3Aen",
            "image_link": "https://lh3.googleusercontent.com/-9QLYdmWUpj3iTBIWZYdBQ9oLNuCrwlPlMLh39xsmp2-crz5MdxUEYHp2b6cRXHmbMNz9b_4XqIuQgqg3g=rj-w512-h512-pf"
        }
    ]
}
    </code>
</pre>


<hr>
rootVIII 2022
