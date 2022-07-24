###### Scrape the latest Google News propaganda!

###### Be sure to run multiple times per day as propaganda changes quickly!


Retrieves Google News links using Selenium Webdriver. Each article's link, title, and OG Image
are scraped. All results are output to a text file as serialized JSON.

This script can help if you need to add a news-feed to your webapp/website with OG preview images.

The script takes 10-15 minutes or so to execute.

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
            "link": "https://www.cnn.com/2022/07/23/politics/zeldin-suspected-attacker-federal-assault-charge/index.html",
            "image_link": "https://cdn.cnn.com/cnnnext/dam/assets/220723143634-zeldin-suspected-attacker-federal-assault-charge-super-tease.jpg"
        },
        {
            "title": "Lee Zeldin's attempted attacker told investigators he 'did not know' speaker's identity",
            "link": "https://www.foxnews.com/politics/lee-zeldins-attempted-attacker-told-investigators-did-not-know-speakers-identity",
            "image_link": "https://static.foxnews.com/foxnews.com/content/uploads/2022/07/Untitled-design-386.png"
        },
        {
            "title": "Trump and Pence duel in Arizona in fight for Republican future",
            "link": "https://www.theguardian.com/us-news/2022/jul/23/trump-pence-arizona-republicans-future-election",
            "image_link": "https://i.guim.co.uk/img/media/65cc0647a34bd7790694a05c744125cae92cb7e5/0_177_3600_2160/master/3600.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=356248d83efc8378529f31895e92fff9"
        }
    ],
    "World": [
        {
            "title": "Russian missiles hit Ukraine port; Kyiv says it is still preparing grain exports",
            "link": "https://www.reuters.com/world/europe/us-pledges-more-military-aid-ukraine-peace-seems-far-off-2022-07-22/",
            "image_link": "https://www.reuters.com/resizer/P_aXjIifEPVoqbUlM7hN2D0pEUk=/1200x628/smart/filters:quality(80)/cloudfront-us-east-2.images.arcpublishing.com/reuters/C6PWX34P4NMVFOHQ6K6SAPHHGE.jpg"
        },
        {
            "title": "Russian missiles strike Odesa one day after grain export deal agreed",
            "link": "https://www.cnn.com/2022/07/23/europe/russia-ukraine-odesa-strike-grain-exports-intl/index.html",
            "image_link": "https://media.cnn.com/api/v1/images/stellar/prod/220723112237-02-odesa-missile-strike-0723.jpg?c=16x9&q=w_800,c_fill"
        },
        {
            "title": "Russian tank attack in eastern Ukraine kills 2 Americans, Canadian and Swede",
            "link": "https://www.politico.com/news/2022/07/23/americans-killed-russian-tank-attack-00047567",
            "image_link": "https://static.politico.com/03/f9/e46d5daa41e1beb268e88fdbc30e/https-delivery.gettyimages.com/downloads/1239284532"
        }
    ],
    "Business": [
        {
            "title": "'Ruffling feathers': How VW fell out of love with Herbert Diess",
            "link": "https://www.ft.com/content/de3858f2-124c-478a-8fad-8540135a4296",
            "image_link": "Failed to find og:image"
        },
        {
            "title": "Why Did VW CEO Herbert Diess Get Fired?",
            "link": "https://www.bloomberg.com/tosv2.html?vid=&uuid=5b191b77-0b0b-11ed-96b9-674b78554664&url=L25ld3MvYXJ0aWNsZXMvMjAyMi0wNy0yMy92dy1zLWJpbGxpb25haXJlLWNsYW4tcGxvdHRlZC1jZW8tb3VzdGVyLXdoaWxlLWhlLXdhcy1vbi11cy10cmlw",
            "image_link": "Failed to find og:image"
        },
        {
            "title": "Dow Jones Futures: Apple Leads Earnings Wave, Fed Rate Hike Looms; What To Do Now | Investor's Business Daily",
            "link": "https://www.investors.com/market-trend/stock-market-today/dow-jones-futures-apple-earnings-fed-rate-hike-headline-huge-market-week-what-to-do-now/",
            "image_link": "Failed to find og:image"
        }
    ],
    "Technology": [
        {
            "title": "Pixel 6a teardown reveals easier battery removal and plastic back [Video]",
            "link": "https://9to5google.com/2022/07/23/pixel-6a-teardown/",
            "image_link": "https://i0.wp.com/9to5google.com/wp-content/uploads/sites/4/2022/07/Pixel-6a-teardown-cover.jpg?resize=1200%2C628&#038;quality=82&#038;strip=all&#038;ssl=1"
        },
        {
            "title": "Google Pixel 6a \u2014 5 reasons to buy and 3 reasons to skip",
            "link": "https://www.tomsguide.com/opinion/google-pixel-6a-reasons-to-buy-and-skip",
            "image_link": "https://cdn.mos.cms.futurecdn.net/FiGh35zHHWDJ6atcwXBPiE-1200-80.jpg"
        },
        {
            "title": "[Let's Talk] Live A Live Switch remake impressions",
            "link": "https://nintendoeverything.com/lets-talk-live-a-live-switch-remake-impressions/",
            "image_link": "https://nintendoeverything.com/wp-content/uploads/live-a-live-impressions-lets-talk.jpg"
        }
    ],
    "Entertainment": [
        {
            "title": "Ben Affleck Appears to Take a Nap on Boat Ride During Post-Wedding Trip With Jennifer Lopez",
            "link": "https://www.eonline.com/news/1339217/ben-affleck-appears-to-take-a-nap-on-boat-ride-during-post-wedding-trip-with-jennifer-lopez",
            "image_link": "Failed to find og:image"
        },
        {
            "title": "Jennifer Lopez Paired a $2290 Dress with $55 Flip Flops for a PDA-Packed Paris Park Date with Ben Affleck",
            "link": "https://people.com/fashion/jennifer-lopez-white-flip-flops-paris/",
            "image_link": "https://imagesvc.meredithcorp.io/v3/mm/image?q=60&c=sc&rect=1%2C97%2C1000%2C597&poi=face&w=1000&h=500&url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F20%2F2022%2F02%2F09%2FBen-and-Jen.jpg"
        },
        {
            "title": "Marvel outlines Phase 6 with Fantastic Four and two new Avengers movies",
            "link": "https://www.theverge.com/2022/7/23/23275861/marvel-phase-6-fantastic-four-avengers-sdcc",
            "image_link": "https://cdn.vox-cdn.com/thumbor/CQhYjIXZnlFxsN-ONAfpYQ2xsDY=/0x715:3000x2286/fit-in/1200x630/cdn.vox-cdn.com/uploads/chorus_asset/file/23895974/FYZK4nLVEAEK0hU.jpg"
        }
    ],
    "Sports": [
        {
            "title": "Sydney McLaughlin shatters 400 hurdles record with 50.68",
            "link": "https://www.foxnews.com/sports/sydney-mclaughlin-shatters-400-hurdles-record-50-68",
            "image_link": "https://static.foxnews.com/foxnews.com/content/uploads/2022/07/AP22204119679839.jpg"
        },
        {
            "title": "Sydney McLaughlin OBLITERATES her own WORLD RECORD for 400 hurdles World Title | NBC Sports",
            "link": "https://www.youtube.com/watch?v=cIlpFhU3P-M",
            "image_link": "https://i.ytimg.com/vi/cIlpFhU3P-M/hqdefault.jpg"
        },
        {
            "title": "Latest On Juan Soto Trade Talks",
            "link": "https://www.mlbtraderumors.com/2022/07/latest-on-juan-soto-trade-talks.html",
            "image_link": "https://cdn.mlbtraderumors.com/files/2022/06/juan-soto-nationals-washington-1024x727.jpg"
        }
    ],
    "Science": [
        {
            "title": "Watch a SpaceX Falcon 9 rocket soar over the moon in incredible tracking cam video",
            "link": "https://www.space.com/spacex-falcon-9-moon-footage-starlink-launch",
            "image_link": "https://cdn.mos.cms.futurecdn.net/7fxHx3iNcg9A6j3PG7vVJo-1200-80.jpg"
        },
        {
            "title": "SpaceX breaks own record with 32nd launch of 2022",
            "link": "https://www.youtube.com/watch?v=JKx1ASLlIDk",
            "image_link": "https://i.ytimg.com/vi/JKx1ASLlIDk/maxresdefault.jpg"
        },
        {
            "title": "Dazzling James Webb Space Telescope image prompts science scramble",
            "link": "https://www.space.com/james-webb-space-telescope-deep-field-science",
            "image_link": "https://cdn.mos.cms.futurecdn.net/cMDRA3454bGvfZASbxviZe-1200-80.jpg"
        }
    ],
    "Health": [
        {
            "title": "Monkeypox officially becomes a global emergency",
            "link": "https://www.cbsnews.com/news/monkeypox-global-health-emergency/",
            "image_link": "https://assets3.cbsnewsstatic.com/hub/i/r/2022/07/20/31035150-da8f-4298-a915-54f39cc09a1a/thumbnail/1200x630/8a46aa48cc13e27b6081e0dd7a7a89f1/pox.jpg"
        },
        {
            "title": "WHO declares monkeypox a public health emergency of international concern",
            "link": "https://www.cnn.com/2022/07/23/health/monkeypox-who-intl/index.html",
            "image_link": "https://media.cnn.com/api/v1/images/stellar/prod/220714153026-monkeypox-questions-update.jpg?c=16x9&q=w_800,c_fill"
        },
        {
            "title": "Polio live oral vaccine: Here's why the US stopped using it years ago",
            "link": "https://nypost.com/2022/07/23/polio-live-oral-vaccine-heres-why-the-us-stopped-using-it-years-ago/",
            "image_link": "https://nypost.com/wp-content/uploads/sites/2/2022/07/AFGHANISTAN_HEALTH_POLIO_VACCINAT_ION-e1658611818205.jpeg?quality=75&#038;strip=all&#038;w=1024"
        }
    ]
}
    </code>
</pre>


<hr>
rootVIII 2022
