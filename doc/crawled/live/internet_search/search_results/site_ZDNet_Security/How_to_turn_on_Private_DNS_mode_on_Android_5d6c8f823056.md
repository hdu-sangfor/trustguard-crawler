# How to turn on Private DNS mode on Android

### 来源信息
- **URL**: https://www.zdnet.com/article/how-to-turn-on-private-dns-mode-on-android-phone/
- **来源站点**: ZDNet Security
- **页面抓取**: 成功

### 页面正文
Why you can trust ZDNET
:ZDNET independently tests and researches products to bring you our best recommendations and advice. When you buy through our links, we may earn a commission.Our process
'ZDNET Recommends': What exactly does it mean?
ZDNET's recommendations are based on many hours of testing, research, and comparison shopping. We gather data from the best available sources, including vendor and retailer listings as well as other relevant and independent reviews sites. And we pore over customer reviews to find out what matters to real people who already own and use the products and services we’re assessing.
When you click through from our site to a retailer and buy a product or service, we may earn affiliate commissions. This helps support our work, but does not affect what we cover or how, and it does not affect the price you pay. Neither ZDNET nor the author are compensated for these independent reviews. Indeed, we follow strict guidelines that ensure our editorial content is never influenced by advertisers.
ZDNET's editorial team writes on behalf of you, our reader. Our goal is to deliver the most accurate information and the most knowledgeable advice possible in order to help you make smarter buying decisions on tech gear and a wide array of products and services. Our editors thoroughly review and fact-check every article to ensure that our content meets the highest standards. If we have made an error or published misleading information, we will correct or clarify the article. If you see inaccuracies in our content, please report the mistake via this form.
Private DNS encrypts your web traffic to prevent ISP tracking.
It improves both privacy and online security.
It's simple to turn on, but disabling it puts your data at risk.
Nearly everything you do on your desktop, laptop, phone, and tablet begins with a Domain Name System (DNS) query. Essentially, DNS turns domain names (such as ZDNET.com) into an IP address so web browsers and apps know where to get the information you want.
Without DNS, you'd have to type 34.149.132.124 every time you wanted to go to ZDNET.com or 74.125.21.102 to go to Google.com. Even by simply running a Google search, DNS is at work. The problem is that standard DNS isn't encrypted, meaning all your queries are sent over the network as plain text.
Why is non-encrypted DNS a problem?
Let's say you're on a public network -- like a coffee shop -- and you start searching for things on your Android device. Or maybe you have to access a CMS or another work tool, and you don't want the public to know the address you're typing. If someone else is on the same network and has the skills, it could intercept your non-encrypted search queries (or the URLs you visit) and know exactly what you're looking for.
That's where Private DNS mode comes into play. Once you enable this feature, all of your DNS queries are encrypted, so bad actors won't be able to view them -- even if it captures those packets. In other words, Private DNS mode should be an absolute must for anyone who values privacy and security.
But how do you enable Private DNS mode on Android? It's actually pretty simple. Let me show you how.
How to enable Private DNS mode (on Android version 11 or newer)
If you're using Android version 11 or newer, the old method of Private DNS no longer works. Instead of handling this process manually, you have to install an application created by Cloudflare called 1.1.1.1 + WARP. Once you've installed that app, it will open, and you'll see a slider marked Disconnected. Tap that slider, and it will enable the service.
There's a caveat to using the app. If it is disabled and you need to re-enable Private DNS, you won't find the app in your app drawer. Instead, you'll have to search for it in the Google Play Store and tap Open from there. I'd like to think Cloudflare could fix this little annoyance, but until it does, you at least know how to access the app. If, on the other hand, the app is running, you'll see a notification entry that, when tapped, will open the app.
How to enable Private DNS mode (on Android versions older than 11)
What you'll need: An Android device running version 10 or older. I'm using a Pixel 9 Pro (which means I now have to use the new method), but pretty much every modern Android phone is capable of enabling Private DNS.
1. Open Network & internet
Open the Settings app (either from the notification shade or the app drawer) and then tap Network & internet. If you're using a Samsung Galaxy device, you'll go to Settings > More Connection Settings.
You'll find the entry for Private DNS near the bottom of the Network & internet window. On Galaxy devices, it will be located in the middle of the More Connection Settings list. If you don't find it, go back to the main Settings page and search for Private DNS.
This is where it can get a bit tricky. You need to have the address of a provider that offers Private DNS. Cloudflare is my provider of choice, so the address for its primary secure DNS is:
Note: Although the above free DNS services are all worth trying, I recommend going with Cloudflare (1dot1dot1dot1.cloudflare-dns.com). I find it the fastest and most secure of the bunch. On top of the speed, Cloudflare adds DNS filtering, which can help prevent email from being sent from malicious IP addresses.
When you tap Private DNS, a new pop-up will appear. Tap Private DNS Provider Hostname, and then type the hostname for the DNS provider of your choice.
You can also choose Automatic, which will automatically switch to Google's Private DNS when it's available. For those who aren't so quick to trust Google for such a feature, I recommend selecting Private DNS and then typing the address for your provider of choice. Tap Save to save the new setting and close the Settings app. You could find yourself in a location where Google's Private DNS servers aren't available, so using one like Cloudflare has advantages beyond speed.
You can then verify it's working by opening your default Android browser and pointing it to http://1.1.1.1/help. If you see "Using DNS over TLS (DoT)" set as "Yes," it's working.
And that's all there is to it. Once you've enabled Private DNS on Android, your DNS queries are encrypted. Enjoy that added privacy and security.

---
*爬取时间: 2026-07-24 15:53:06*
*来源: 直接站点爬取*
