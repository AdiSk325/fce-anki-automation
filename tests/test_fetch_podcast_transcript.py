import unittest

import helpers  # noqa: F401  (dodaje scripts/ do sys.path)

import fetch_podcast_transcript as f

PAGE = """
<html><head><title>Episode 1 | Podcast</title><script>var x = 1;</script></head>
<body><article>
<h1>Episode 1: Learning habits</h1>
<p>Intro text about the show.</p>
<h2>Transcript</h2>
<p>Hello and welcome to the show.</p>
<p>Today we talk about habits.<br>Habits are hard to change.</p>
<p>Let's get started.</p>
<p>Thanks for listening and see you next time.</p>
<p>Support this podcast on Patreon.</p>
</article></body></html>
"""


class UrlValidationTest(unittest.TestCase):
    def test_accepts_public_https(self):
        f.validate_remote_url("https://thinkinginenglish.blog/episode-1")

    def test_rejects_unsafe_urls(self):
        for url in ["ftp://example.com/x", "http://localhost/x", "http://127.0.0.1/x", "http://10.0.0.5/x", "https:///x"]:
            with self.subTest(url=url), self.assertRaises(ValueError):
                f.validate_remote_url(url)


class ExtractionTest(unittest.TestCase):
    def test_transcript_section_between_heading_and_stop_phrase(self):
        lines = f.html_to_lines(f.extract_article_html(f.strip_html_blocks(PAGE)))
        transcript, note = f.find_transcript_lines(lines)
        self.assertEqual(transcript, [
            "Hello and welcome to the show.",
            "Today we talk about habits.",
            "Habits are hard to change.",
            "Let's get started.",
        ])
        self.assertIn("heading found", note)

    def test_title_and_slug(self):
        self.assertEqual(f.detect_title(PAGE, "fallback"), "Episode 1: Learning habits")
        self.assertEqual(f.slug_from_url("https://site.com/podcast/Episode_12-Habits/"), "episode-12-habits")


if __name__ == "__main__":
    unittest.main()
