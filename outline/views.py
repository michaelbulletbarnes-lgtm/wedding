# outline/views.py
from django.shortcuts import render

PROGRAM_DATA = {
    "cover": {
        "couple": "Ernest & Eunice",
        "date": "November 21, 2026",
        "hashtag": "#ErnestAndEunice2026" # Added for a modern touch
    },
    "wedding_party": {
        "maid_of_honour": "Esther Asiedu",
        "best_man": "Wisdom Adzamani"
    },
    "officiating_ministers": [
        {"name": "Very Rev. Kwesi Amissah-Essel", "role": "Supt Minister, Bisease Circuit"},
        {"name": "Rev. Joseph Kwamena Tawiah", "role": "Bisease District Minister (Presby)"},
        {"name": "Rev. Sydney Odotei Akonor", "role": "Enyan Denkyira (Presby)"},
        {"name": "Rev. Paul Frederick Adjei", "role": "Retired Presby Minister"},
        {"name": "Rev. Harrison Amponsah", "role": "District Minister, Akyem Awusa (Presby)"},
        {"name": "Rev. Father Christian Ninson", "role": "Breman Esikuma"},
        {"name": "Apostle Michael Akese", "role": "Bisease"}
    ],
    "others": [
        {"name": "Bro. Ebenezer Essandor", "role": "Ministerial Student"},
        {"name": "Evangelist Frederick Ekow Baah", "role": "Circuit Evangelist"},
        {"name": "Bro Eric Gyesi", "role": "Circuit Steward"},
        {"name": "Bro. J. K. Mensah", "role": "Society Steward"},
        {"name": "Bro. Emmanuel Dadzie", "role": "Society Steward"},
        {"name": "Sis. Ernestina Agyeman", "role": "Society Steward"}
    ],
    "protocol": ["Mavis Hanson", "Ebenezer Tawiah"],
    "order_of_service": [
        "Bridal Procession", "Call To Worship", "Opening Hymn - CAN 92 MHB 314",
        "Opening Prayer", "Declaration Of Purpose", "Legal Declaration", "Vows",
        "Hymn Of Dedication - CAN 131 MHB 400", "Giving Of Rings", "Pronouncement Of Marriage",
        "Prayer", "Hymn - CAN 199 MHB 608", "Ministry Of The Word", 
        "Hymn - CAN 90 MHB 308", "Sermon", "Holy Communion - CAN 113 MHB 351",
        "Anthem - Choir", "Announcement", "Offering - Singing Band",
        "Signing Of Certificate And Offertory - Singing Band",
        "Presentation Of Marriage Certificate and Love Offering",
        "Closing Hymn - CAN 198 MHB 607", "Closing Prayer And Benediction",
        "Bridal Recession - CAN 201 MHB 611"
    ],
    "photography": [
        "Officiating Ministers", "Catechists / Caretakers Conference", "Groom's Family",
        "Bride's Family", "Both Family", "Presby Church, Brofoyedur",
        "Methodist Church Members", "Presby Church, Bisease", "Bisease Polyclinic Staff",
        "Treds of Unity Members", "District J.Y. Leaders", "Y.P.G. Members",
        "Groom's Friends/ Class Mates", "Bride's Friends / Class Mates"
    ],
    "reception": [
        "Opening Prayer - Cat. Albert Baidoo", "Musical Interlude - D.J.",
        "Arrival of Couple", "Musical Interlude - D.J.", "Solo - Minister Grace",
        "Intro. of Chairman & Supporters - Miss. Priscilla Acquah", "Chairman's Response",
        "Musical Interlude", "Solo - Min. Christy / Lois", "Dance by Couple",
        "Presentation of Gift", "Cake Cutting/Poping of Champaign", "Refreshment",
        "Chairman's Closing Remarks", "Vote of Thanks - Winifred Baidoo",
        "Picture Taking", "Closing Prayer - Cat. Francis Baidoo"
    ],
    "thank_you": {
        "message": "Thank you for your enormous support and contributions to our Wedding Celebration. We know that you moved mountains to be with us and we are very grateful. We appreciate you.",
        "signature": "Mr. & Mrs Botwey"
    }
}

def index(request):
    return render(request, "outline/index.html", {"data": PROGRAM_DATA})