from fastapi import FastAPI, Request
from fastapi.responses import Response

from intent_engine import detect_intent
from backend_service import get_pnr_status, get_train_schedule
from response_formatter import format_pnr_response, format_train_response

app = FastAPI()


def menu():
    return """
    <Gather input="speech"
    speechTimeout="auto"
    language="en-IN"
    hints="pnr, p n r, train number, train schedule"
    action="/twilio-webhook"
    method="POST">

        <Say>
        You can say check P N R status,
        check train schedule,
        book ticket,
        cancel ticket,
        or end call.
        </Say>

    </Gather>
    """


@app.post("/twilio-webhook")
async def twilio_webhook(request: Request):

    form = await request.form()
    speech = form.get("SpeechResult")

    print("Speech:", speech)

    if not speech:

        twiml = f"""
        <Response>
            <Say>Welcome to IRCTC voice assistant.</Say>
            {menu()}
        </Response>
        """

        return Response(content=twiml, media_type="application/xml")

    speech = speech.lower()
    intent = detect_intent(speech)


    # END CALL
    if intent == "END_CALL":

        twiml = """
        <Response>
            <Say>Thank you for calling IRCTC. Goodbye.</Say>
            <Hangup/>
        </Response>
        """

        return Response(content=twiml, media_type="application/xml")


    # PNR FLOW
    if intent == "PNR_STATUS":

        twiml = """
        <Response>

            <Gather input="speech"
            speechTimeout="auto"
            language="en-IN"
            hints="zero one two three four five six seven eight nine"
            action="/process-pnr"
            method="POST">

                <Say>Please say your ten digit P N R number.</Say>

            </Gather>

        </Response>
        """

        return Response(content=twiml, media_type="application/xml")


    # TRAIN FLOW
    if intent == "TRAIN_SCHEDULE":

        twiml = """
        <Response>

            <Gather input="speech"
            speechTimeout="auto"
            language="en-IN"
            hints="zero one two three four five six seven eight nine"
            action="/process-train"
            method="POST">

                <Say>Please say your five digit train number.</Say>

            </Gather>

        </Response>
        """

        return Response(content=twiml, media_type="application/xml")


    # BOOK TICKET
    if intent == "BOOK_TICKET":

        twiml = f"""
        <Response>
            <Say>
            Ticket booking is available on the IRCTC website
            or mobile application.
            </Say>
            {menu()}
        </Response>
        """

        return Response(content=twiml, media_type="application/xml")


    # CANCEL TICKET
    if intent == "CANCEL_TICKET":

        twiml = f"""
        <Response>
            <Say>
            Your ticket cancellation request has been initiated.
            </Say>
            {menu()}
        </Response>
        """

        return Response(content=twiml, media_type="application/xml")


    twiml = f"""
    <Response>
        <Say>Sorry I did not understand.</Say>
        {menu()}
    </Response>
    """

    return Response(content=twiml, media_type="application/xml")


# PROCESS PNR
@app.post("/process-pnr")
async def process_pnr(request: Request):

    form = await request.form()
    speech = form.get("SpeechResult")

    print("PNR speech:", speech)

    pnr = "".join(filter(str.isdigit, speech))

    data = get_pnr_status(pnr)
    message = format_pnr_response(data)

    twiml = f"""
    <Response>
        <Say>{message}</Say>
        {menu()}
    </Response>
    """

    return Response(content=twiml, media_type="application/xml")


# PROCESS TRAIN
@app.post("/process-train")
async def process_train(request: Request):

    form = await request.form()
    speech = form.get("SpeechResult")

    print("Train speech:", speech)

    train = "".join(filter(str.isdigit, speech))

    data = get_train_schedule(train)
    message = format_train_response(data)

    twiml = f"""
    <Response>
        <Say>{message}</Say>
        {menu()}
    </Response>
    """

    return Response(content=twiml, media_type="application/xml")