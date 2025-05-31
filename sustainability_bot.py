from flask import Flask, request, jsonify

app = Flask(__name__)

SUSTAINABILITY_DB = {
    "plastic": {
        "recycle": "♻️ Clean and dry plastic containers before recycling. Remove caps.",
        "reuse": "🎨 Make art & crafts from bottles! Also great for farming & planters.",
        "ideas": "💡 AI suggests: Use waste plastic for vertical gardening or as plant supports."
    },
    "food waste": {
        "reuse": "🌱 Turn food scraps into compost for farming/agriculture!",
        "ideas": "💡 AI suggests: Use peels for natural fertilizers, or bio-gas generation."
    },
    "e-waste": {
        "recycle": "📱 Find certified e-waste recyclers for proper disposal.",
        "reuse": "💡 Turn old phones into music players, cameras, or mini screens.",
        "ideas": "💡 AI suggests: Use parts for DIY sensors or mini green tech projects."
    }
}

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    response = {"text": "", "suggestions": []}

    if "hi" in user_input or "hello" in user_input:
        response["text"] = "👋 Hii! How can I help you with Eco City and Green City ideas?"
    elif "why are eco-cities important" in user_input:
        response["text"] = (
            "🏙️ Great question! Eco-cities create healthier lives while protecting our planet:\n\n"
            "Cleaner Air - Bengaluru reduced pollution by 30% with urban forests\n"
            "Water Wisdom - Chennai saves 40% water with smart harvesting\n"
            "Waste to Wealth - Indore turns 90% trash into reusable resources\n"
            "Green Jobs - Surat created 5,000 jobs in solar energy\n\n"
            "Want me to suggest how YOUR city can improve? Just share its name!"
        )
    elif "tell me about" in user_input:
        city_name = user_input.replace("tell me about", "").strip().capitalize()
        response["text"] = (
            f"📊 Here's how we can transform {city_name} together:\n\n"
            "🌳 Green Infrastructure\n• Convert 3 abandoned lots into urban farms\n"
            "• Plant native trees along all main roads\n\n"
            "⚡ Clean Energy\n• Install solar panels on govt buildings first\n"
            "• Start community solar cooperatives\n\n"
            "🚲 Smart Mobility\n• Electric shuttle buses between markets\n"
            "• Bicycle repair stations every 2km\n\n"
            "♻️ Waste Solutions\n• Weekly 'upcycling' workshops\n"
            "• App for trading unused items"
        )
    elif "plastic" in user_input:
        response["text"] = SUSTAINABILITY_DB["plastic"]["recycle"]
        response["suggestions"].extend([
            SUSTAINABILITY_DB["plastic"]["reuse"],
            SUSTAINABILITY_DB["plastic"]["ideas"]
        ])
    elif "food" in user_input or "waste" in user_input:
        response["text"] = SUSTAINABILITY_DB["food waste"]["reuse"]
        response["suggestions"].append(SUSTAINABILITY_DB["food waste"]["ideas"])
    elif "e-waste" in user_input or "electronic" in user_input:
        response["text"] = SUSTAINABILITY_DB["e-waste"]["recycle"]
        response["suggestions"].extend([
            SUSTAINABILITY_DB["e-waste"]["reuse"],
            SUSTAINABILITY_DB["e-waste"]["ideas"]
        ])
    else:
        response["text"] = (
            "🌿 I can help with:\n"
            "🔹 Make your city greener\n"
            "🔸 Find recycling/composting spots\n"
            "🔹 Get energy-saving tips\n"
            "🔸 Learn about urban sustainability projects\n\n"
            "What would you like to explore first?"
        )

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000)
