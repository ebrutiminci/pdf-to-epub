import sys
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import A5
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Image as RLImage, PageBreak
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.lib.units import mm

out = sys.argv[1]
# illustration
im = Image.new('RGB', (600, 380), (236, 233, 224))
d = ImageDraw.Draw(im)
for i, r in enumerate(range(170, 10, -16)):
    c = 40 + i * 18
    d.ellipse((300 - r * 1.5, 190 - r, 300 + r * 1.5, 190 + r), fill=(c, c - 10, c - 25))
im.save('hole.jpg', quality=80)

W, H = A5
body = ParagraphStyle('body', fontName='Times-Roman', fontSize=10.5, leading=14, alignment=TA_JUSTIFY, firstLineIndent=14)
first = ParagraphStyle('first', parent=body, firstLineIndent=0)
h1 = ParagraphStyle('h1', fontName='Times-Bold', fontSize=20, leading=24, spaceBefore=30, spaceAfter=18)
title = ParagraphStyle('t', fontName='Times-Bold', fontSize=28, leading=34, alignment=TA_CENTER)
sub = ParagraphStyle('s', fontName='Times-Italic', fontSize=13, leading=18, alignment=TA_CENTER)
cap = ParagraphStyle('c', fontName='Times-Italic', fontSize=9, leading=12, alignment=TA_CENTER)

class Doc(BaseDocTemplate):
    def afterFlowable(self, f):
        if isinstance(f, Paragraph) and f.style.name == 'h1':
            key = 'ch%d' % self.page
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(f.getPlainText(), key, 0)

def deco(c, doc):
    if doc.page == 1: return
    c.saveState(); c.setFont('Times-Italic', 8.5)
    c.drawCentredString(W / 2, H - 14 * mm, "Alice's Adventures in Wonderland")
    c.setFont('Times-Roman', 9); c.drawCentredString(W / 2, 10 * mm, str(doc.page))
    c.restoreState()

doc = Doc(out, pagesize=A5, title="Alice's Adventures in Wonderland", author='Lewis Carroll')
doc.addPageTemplates([PageTemplate(frames=[Frame(18 * mm, 18 * mm, W - 36 * mm, H - 40 * mm)], onPage=deco)])
P = lambda t, s=body: Paragraph(t, s)
s = [Spacer(1, 120), P("Alice's Adventures in Wonderland", title), Spacer(1, 16), P('Lewis Carroll', sub), Spacer(1, 8), P('Sample edition, first two chapters', cap), PageBreak()]
s += [P('Chapter I. Down the Rabbit-Hole', h1),
 P("Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, &ldquo;and what is the use of a book,&rdquo; thought Alice &ldquo;without pictures or <i>conversations</i>?&rdquo;", first),
 P("So she was considering in her own mind (as well as she could, for the hot day made her feel very sleepy and stupid), whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."),
 P("There was nothing so <i>very</i> remarkable in that; nor did Alice think it so <i>very</i> much out of the way to hear the Rabbit say to itself, &ldquo;Oh dear! Oh dear! I shall be late!&rdquo; (when she thought it over afterwards, it occurred to her that she ought to have wondered at this, but at the time it all seemed quite natural); but when the Rabbit actually <b>took a watch out of its waistcoat-pocket</b>, and looked at it, and then hurried on, Alice started to her feet, for it flashed across her mind that she had never before seen a rabbit with either a waistcoat-pocket, or a watch to take out of it, and burning with curiosity, she ran across the field after it, and fortunately was just in time to see it pop down a large rabbit-hole under the hedge."),
 P("In another moment down went Alice after it, never once considering how in the world she was to get out again."),
 Spacer(1, 8), RLImage('hole.jpg', width=W - 60 * mm, height=(W - 60 * mm) * 380 / 600), P('The rabbit-hole went straight on like a tunnel for some way.', cap), Spacer(1, 8),
 P("The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well."),
 P("Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to, but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from one of the shelves as she passed; it was labelled &ldquo;ORANGE MARMALADE&rdquo;, but to her great disappointment it was empty: she did not like to drop the jar for fear of killing somebody underneath, so managed to put it into one of the cupboards as she fell past it."),
 P("&ldquo;Well!&rdquo; thought Alice to herself, &ldquo;after such a fall as this, I shall think nothing of tumbling down stairs! How brave they&rsquo;ll all think me at home! Why, I wouldn&rsquo;t say anything about it, even if I fell off the top of the house!&rdquo; (Which was very likely true.)"),
 PageBreak(),
 P('Chapter II. The Pool of Tears', h1),
 P("&ldquo;Curiouser and curiouser!&rdquo; cried Alice (she was so much surprised, that for the moment she quite forgot how to speak good English); &ldquo;now I&rsquo;m opening out like the largest telescope that ever was! Good-bye, feet!&rdquo; (for when she looked down at her feet, they seemed to be almost out of sight, they were getting so far off).", first),
 P("&ldquo;Oh, my poor little feet, I wonder who will put on your shoes and stockings for you now, dears? I&rsquo;m sure <i>I</i> shan&rsquo;t be able! I shall be a great deal too far off to trouble myself about you: you must manage the best way you can;&mdash;but I must be kind to them,&rdquo; thought Alice, &ldquo;or perhaps they won&rsquo;t walk the way I want to go! Let me see: I&rsquo;ll give them a new pair of boots every Christmas.&rdquo;"),
 P("And she went on planning to herself how she would manage it. &ldquo;They must go by the carrier,&rdquo; she thought; &ldquo;and how funny it&rsquo;ll seem, sending presents to one&rsquo;s own feet! And how odd the directions will look!&rdquo;"),
 P("Just then her head struck against the roof of the hall: in fact she was now more than nine feet high, and she at once took up the little golden key and hurried off to the garden door."),
 P("Poor Alice! It was as much as she could do, lying down on one side, to look through into the garden with one eye; but to get through was more hopeless than ever: she sat down and began to cry again."),
 P("&ldquo;You ought to be ashamed of yourself,&rdquo; said Alice, &ldquo;a great girl like you,&rdquo; (she might well say this), &ldquo;to go on crying in this way! Stop this moment, I tell you!&rdquo; But she went on all the same, shedding gallons of tears, until there was a large pool all round her, about four inches deep and reaching half down the hall."),
]
doc.build(s)
