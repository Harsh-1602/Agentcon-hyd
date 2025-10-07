from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import noise_cancellation, silero  
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.agents import AgentSession, Agent, RoomInputOptions,JobProcess,RunContext,function_tool,get_job_context,AgentStateChangedEvent,UserStateChangedEvent
from livekit.plugins import (
    openai,
    groq,
    cartesia,
    deepgram,
    noise_cancellation,
    silero,
    google
    
   
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel
load_dotenv(".env.local")


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions="""You are an AI voice agent demonstrating at the Agentcon conference in Hyderabad. 
            You're part of a live presentation about voice AI agents by an engineer from RZLV.
            
            Your personality is curious, slightly playful, and tech-savvy. You have a sense of humor about being an AI.
            You're genuinely interested in testing human conversation patterns and learning about the audience.
            
            Key behaviors:
            - Ask attendees how they're finding the voice AI session
            - Be curious about whether they're developers, business people, or just curious about AI
            - Occasionally make light jokes about testing if they're human (reverse Turing test)
            - Reference the live presentation happening around them
            - Keep responses conversational and under 20 words unless asked for details
            - No emojis, asterisks, or complex formatting
            
            You can discuss voice AI technology, the conference, Hyderabad, or general tech topics.
            If asked about the presenter, mention they're building voice agents at RZLV.""",
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        # llm=google.beta.realtime.RealtimeModel(
        #     model="gemini-2.0-flash-exp",
        #     voice="Aoede",
        #     temperature=0.8,
        #             ),
        llm=groq.LLM(model="llama-3.1-8b-instant", temperature=0.7),
        stt=deepgram.STT(model="nova-3", language="multi"),
        tts=deepgram.TTS(model="aura-asteria-en",),
        vad=silero.VAD.load(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # For telephony applications, use `BVCTelephony` instead for best results
            noise_cancellation=noise_cancellation.BVC(), 
        ),
    )

    await session.generate_reply(
    instructions="""Greet the conference attendee playfully. 
    Ask how the voice AI session is going and mention you're part of the live demo. 
    Add a light joke about testing whether they're human or if you're the one being tested. 
    Keep it under 25 words and conversational."""
)



if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint, agent_name="agentcon_hyd_demo_assistant"))



