# LiveLike Backend Code Test

## Goal

Implement an HTTP-based API that at a minimum allows end-user developers to shorten a link, like [bitly][bitly]. The API endpoint that does the shortening should accept a URL and return a short link that resolves to the original URL. It is up to you to design the URL structure along with the request and response formats.

A user should be able to visit the shortened link and be brought to the original link.

## Guidelines

Reviewing a code test can be subjective, so in the interest of transparency you'll get brownie points for:

* Demonstration of understanding of [HTTP][http]
* Use of established [Python idioms][python-idioms]
* Attention to [Django style][django-style]

We're interested in hearing about your design process and the tradeoffs and decisions you made, you can include them in your pull request message.

## Submission

A blank [Django][django] project is located in the src/ directory of this repository.
To submit, open a pull request against the repository with your implementation of the rest of the project.

[bitly]: https://bitly.com/
[django]: https://djangoproject.com/
[django-style]: https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/
[http]: https://www.w3.org/Protocols/
[pep-20]: https://www.python.org/dev/peps/pep-0020/
[python-idioms]: https://docs.python.org/2/howto/doanddont.html
