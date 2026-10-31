# Reflow: PDF to EPUB

A PDF to EPUB converter that runs entirely in the browser. PDFs are never uploaded: reading, converting and packaging all happen on your device.

It is a single static page (`index.html`), so it can be hosted anywhere, including GitHub Pages.

## What it does

- Rejoins PDF lines into real paragraphs, repairs words hyphenated at line ends, and keeps paragraphs whole across page and column breaks
- Removes running headers and page numbers
- Builds chapters and a nested table of contents from the PDF's bookmarks, or from large and bold headings when there are none
- Keeps bold, italic and superscripts; moves footnotes out of the running text
- Cuts figures and photos out of the page; keeps pages without text (plates, scans) as images
- Uses page 1 as the cover, or an image you upload
- Reads scanned PDFs with text recognition (OCR, via [Tesseract](https://github.com/naptha/tesseract.js)) in 14 languages including English and Turkish, and keeps photos found on scanned pages
- Offers a fixed-layout "Page images" EPUB for comics, magazines and scans you want to keep exactly as they look
- Opens password-protected PDFs; supports page ranges
- Shows a chapter-by-chapter proof before you download

Output is EPUB 3 with an EPUB 2 `toc.ncx` for older readers. It opens in Apple Books, Kobo, Google Play Books and Calibre, and on Kindle via Send to Kindle. Test conversions pass [EPUBCheck](https://github.com/w3c/epubcheck) with no errors or warnings.

## Use it

Open `index.html` in a browser, or publish it with GitHub Pages: **Settings → Pages → Deploy from a branch → `main` / root**. The page loads [pdf.js](https://mozilla.github.io/pdf.js/), [JSZip](https://stuk.github.io/jszip/) and, for scanned pages, [Tesseract.js](https://github.com/naptha/tesseract.js) and its language data from the jsDelivr CDN, so it needs an internet connection to start. The language data (2–4 MB) is cached in the browser after the first use.

## Limits

- Text recognition is accurate on clean print (about 99% of words in tests) but slower: a few seconds per page. It can misread faded, skewed or handwritten pages, italics, and unusual fonts. Bold and italic are not recognised in scans.
- Inside the claude.ai preview, text recognition cannot download its language data; use the GitHub Pages site.
- Tables and vector charts come out as lines of text; labels inside diagrams may mix into the text.
- Complex magazine-style layouts convert better with the Page images layout.

## Development

- `tools/make_sample.py` builds the sample PDF (public-domain text from *Alice's Adventures in Wonderland*) with ReportLab and Pillow.
- `tools/embed_sample.py index.html sample.pdf` embeds that PDF into the page for the "Try the sample book" button.
