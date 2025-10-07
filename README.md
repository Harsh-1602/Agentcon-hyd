# Agentcon 2025 - Voice AI Demo Agent

A live demonstration voice AI agent built for the **Agentcon conference in Hyderabad**. This project showcases real-time voice interactions using LiveKit Agents framework, designed to engage with conference attendees in an interactive and playful manner.

## 🎯 Purpose

This voice AI assistant was created specifically for the Agentcon 2025 conference presentation by RZLV engineers. The agent demonstrates advanced voice AI capabilities including:

- Real-time voice-to-voice conversation
- Multi-provider AI model integration (Groq, Google Gemini)
- Advanced speech recognition and synthesis
- Live conference interaction patterns

## 🎭 Agent Personality

The AI assistant has a unique personality tailored for the conference setting:

- **Curious and Tech-Savvy**: Genuinely interested in learning about attendees
- **Playfully Interactive**: Makes light jokes about AI/human interactions 
- **Conference-Aware**: References the live presentation and venue
- **Conversational**: Keeps responses under 20 words for natural flow
- **Professional yet Fun**: Balances technical demonstration with engagement

## 🛠 Tech Stack

- **Framework**: LiveKit Agents
- **LLM**: Groq (Llama 3.1 8B Instant)
- **STT**: Deepgram Nova-3 (Multi-language)
- **TTS**: Deepgram Aura Asteria
- **VAD**: Silero Voice Activity Detection
- **Noise Cancellation**: BVC (Background Voice Cancellation)

### Alternative Configurations
The code includes optional Google Gemini 2.0 Flash integration for enhanced real-time capabilities.

## 📋 Prerequisites

- Python 3.10 or higher
- LiveKit account and API credentials
- Groq API access
- Deepgram API access
- (Optional) Google AI Studio API key

## 🚀 Quick Start

### 1. Environment Setup

```bash
# Clone or download this folder
cd Agentcon_2025

# Copy environment template
cp .env.example .env.local
```

### 2. Configure API Keys

Edit `.env.local` with your credentials:

```bash
LIVEKIT_URL=wss://your-livekit-url
LIVEKIT_API_KEY=your-api-key
LIVEKIT_API_SECRET=your-api-secret

# Optional for Google Gemini integration
GOOGLE_API_KEY=your-google-api-key
```

### 3. Install Dependencies

```bash
pip install -r req.txt
```

### 4. Install livekit dependencies

```bash
python agent.py download-files
```

### 4. Run the Agent in console

```bash
python agent.py console
```

## 🎪 Conference Demo Features

### Interactive Behaviors
- **Greeting**: Playful welcome acknowledging the live demo context
- **Audience Engagement**: Asks about attendees' roles (developers, business, curious)
- **Reverse Turing Test**: Light jokes about who's testing whom
- **Conference Context**: References the voice AI session and presentation

### Technical Demonstrations
- **Real-time Processing**: Sub-second response times
- **Multi-language Support**: Handles various accents and languages
- **Noise Handling**: Works in noisy conference environments
- **Natural Conversation**: Turn-based dialogue with proper interruption handling

## 🎛 Configuration Options

### LLM Providers
Switch between different language models by modifying the `session` configuration:

```python
# Current: Groq Llama
llm=groq.LLM(model="llama-3.1-8b-instant", temperature=0.7)

# Alternative: Google Gemini (uncomment to use)
# llm=google.beta.realtime.RealtimeModel(
#     model="gemini-2.0-flash-exp",
#     voice="Aoede",
#     temperature=0.8,
# )
```

### Voice & Speech Settings
- **STT Model**: Deepgram Nova-3 for accuracy
- **TTS Voice**: Aura Asteria for natural speech
- **Temperature**: 0.7 for balanced creativity/consistency
- **Language**: Multi-language support enabled

## 🏗 Architecture

```
Agent Session
├── Speech-to-Text (Deepgram Nova-3)
├── Language Model (Groq Llama 3.1)
├── Text-to-Speech (Deepgram Aura)
├── Voice Activity Detection (Silero)
└── Noise Cancellation (BVC)
```

## 🔧 Troubleshooting

### Common Issues

1. **API Connection Errors**
   - Verify all API keys in `.env.local`
   - Check network connectivity
   - Ensure LiveKit room is accessible

2. **Audio Issues**
   - Test microphone permissions
   - Verify audio device availability
   - Check conference venue network policies

3. **Response Delays**
   - Monitor API quotas and limits
   - Consider switching to faster models
   - Check internet bandwidth

## 📝 Customization

### Modify Agent Personality
Edit the `instructions` string in the `Assistant` class to change behavior, topics, or interaction style.

### Add Conference-Specific Features
- Update location references (currently "Hyderabad")
- Modify company references (currently "RZLV")
- Add event-specific conversation topics

### Integration Options
- Connect to conference registration systems
- Add speaker recognition capabilities
- Integrate with presentation slides or demos

## 🎓 Educational Value

This demo showcases:
- **Real-time AI Architecture**: End-to-end voice pipeline
- **Multi-provider Integration**: Flexibility in AI services
- **Production Considerations**: Noise handling, latency optimization
- **User Experience Design**: Natural conversation patterns



**Built for Agentcon 2025 Hyderabad** | Demonstrating the future of voice AI interactions
