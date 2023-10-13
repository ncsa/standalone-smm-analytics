import html

links = {
'single-word': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/AutoPhrase_single-word.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=36dd36243b2986a89521413d1b56fd9f7533a0b861e760a10b8b481d24018167',
'model': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/segmentation.model?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=17804b5e3766e1ea762660b1ada9beb9ff3bbe10f207987a78d7df38c2f4653c',
'autophrase': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/AutoPhrase.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=7454ed576ba427329faf631876beb5312e26a20f2c2dd6f26579dacd836b9f3d',
'visualization': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/div.html?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e5813e686b08a879defc22a7a4c0675caadb736dab05319e48c5b2dde4260fdc',
'multi-words': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/AutoPhrase_multi-words.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=38fac737f0f84d8e02a4e00374738fad678140d008c6acf8503c38b2ace3bdc3',
'token-mapping': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/token_mapping.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=f8db002ab6f07ae1c84ea4c49741c2147c6926a8758739aedf8df801038cdb2f',
'config': 'http://141.142.218.143:9000/macroscope-smile/ywkim%40illinois.edu/NLP/autophrase/b5dbd0de-09d3-4d9a-8629-905b82ed957e/config.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIFVGPPZEGB5JG3UQ%2F20231012%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231012T174952Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=6629785ba5ad3e92f82bf38f73a1f6c8181a3e8917328642e23753ea98b8fec1'
}
fpath = ["a", "b", "c", "d"]
test_url = ["http://test.com"]

list_html = ''
for key in links.keys():
    list_html += '<li><a href="' + links[key] + '">' + key + '</a></li>'

print(list_html)

html = f"""<html>
        <head></head>
        <body style="font-size:15px;font-fiamily:'Times New Roman', Times, serif;">
            <div>
                <p>Dear user (session ID: {fpath[0]}),</p>
                <p>Your {fpath[2]} results are ready for you! (job ID: {fpath[3]})</p>
                <ul>
                    <li>You can view the visualization and download the results at <b>Past Results</b> page in SMILE.
                    <a href={test_url}>Go to your session.</a>
                    <ul>
                        <li>Go to <b>Past Results</b></li>
                        <li>--> under <b>{fpath[1]}</b> tab</li>
                        <li>--> click <b>{fpath[2]}</b></li>
                        <li>--> then find <b>{fpath[3]}</b></li>
                        <li>--> click <b>view</b></li>
                    </ul>
                    <br>
                    <li>You can also click the link below to download part of the results:
                        <ul>{list_html}</ul>
                    </li>
                </ul>
                <br>
                <p>Best Regards,</p>
                <p>Social Media Macroscope - SMILE </p>
            </div>
        </body>
</html>"""

print(html)