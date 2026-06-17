from database import (
    get_favorites,
    get_search_history,
    get_price_history
)

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime
import os
from utils import pause

BASE_DIR = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

REPORT_DIR = os.path.join( BASE_DIR,"reports")

os.makedirs(REPORT_DIR,exist_ok=True) 

def generate_report():

    favorites = get_favorites()
    searches = get_search_history()
    price_history = get_price_history()

    total_favorites = len(favorites)
    total_searches = len(searches)
    total_price_records = len(price_history)

    if not price_history:
        highest_price = 0
        lowest_price = 0
        average_price = 0
     
    else :
        prices = []   

        for record in price_history:
            prices.append(record[2])

        highest_price = max(prices)
        lowest_price =  min(prices)
        average_price = round(sum(prices)/len(prices),2)

    generated_time = datetime.now()

    display_timestamp = generated_time.strftime(
        "%d-%b-%Y %H:%M:%S"
    )

    file_timestamp = generated_time.strftime(
        "%Y-%m-%d_%H-%M-%S"
    )


    pdf_file = os.path.join(REPORT_DIR,
        f"shopwise_report_{file_timestamp}.pdf"
    )

    doc = SimpleDocTemplate(pdf_file)

    styles = getSampleStyleSheet()

    content = []   

    content.append(Paragraph("SHOPWISE REPORT",styles["Title"]))

    content.append(Spacer(1, 12))

    content.append(
    Paragraph(f"Generated On: {display_timestamp}",styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph("SUMMARY",styles["Heading2"]))

    content.append(Spacer(1, 12))

    content.append( Paragraph(f"Total Favorites: {total_favorites}",styles["Normal"]))

    content.append( Paragraph( f"Total Searches: {total_searches}",styles["Normal"]))

    content.append(Paragraph( f"Total Price Records: {total_price_records}", styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(
    Paragraph("ANALYTICS SUMMARY",styles["Heading2"]))

    content.append(Spacer(1, 12))

    content.append( Paragraph( f"Highest Recorded Price: ${highest_price:.2f}",styles["Normal"]))

    content.append(Paragraph(f"Lowest Recorded Price: ${lowest_price:.2f}",styles["Normal"]))

    content.append(Paragraph( f"Average Recorded Price: ${average_price:.2f}", styles["Normal"]))

    content.append(Spacer(1, 12))

    content.append(Paragraph( "End of Report", styles["Italic"]))

    doc.build(content)

    print( f"Report generated successfully: {pdf_file}")
    pause()

generate_report()    