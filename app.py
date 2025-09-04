
import gradio as gr
from diffusers import StableDiffusionPipeline
import torch
from PIL import Image

# Stable Diffusion Pipeline Setup
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def build_prompt(
    mood, season, gender, audience, garment, silhouette, color, material, environment,
    influence, narrative
):
    prompt = f"An entirely original, imaginative digital fashion design. "
    prompt += f"Mood: {mood}. Season: {season}. Gender Expression: {gender}. "
    prompt += f"Target Audience: {audience}. Garment Type: {garment}. "
    prompt += f"Silhouette Style: {silhouette}. Color Palette: {color}. "
    prompt += f"Material Concept: {material}. Environment Context: {environment}. "
    if influence:
        prompt += f"Cultural or Artistic Influence: {influence}. "
    if narrative:
        prompt += f"Narrative Element: {narrative}. "
    prompt += "The design must reflect a unique aesthetic vision and push creative boundaries in form, texture, and concept. Ethically original, not derivative of any existing fashion brand or designer. Conceptual art."
    return prompt

def generate_image(
    mood, season, gender, audience, garment, silhouette, color, material, environment,
    influence, narrative, guidance_scale
):
    prompt = build_prompt(
        mood, season, gender, audience, garment, silhouette, color, material, environment,
        influence, narrative
    )
    image = pipe(prompt, guidance_scale=guidance_scale).images[0]
    return image

with gr.Blocks() as demo:
    gr.Markdown("# Digital Fashion Generator - Creative & Ethical")
    gr.Markdown("Generate a digital fashion design that is entirely original, imaginative, and ethically sourced.")
    with gr.Row():
        with gr.Column():
            mood = gr.Dropdown(["ethereal", "rebellious", "melancholic", "futuristic"], label="Mood", value="ethereal")
            season = gr.Dropdown(["Spring/Summer", "Fall/Winter", "timeless", "post-seasonal"], label="Season", value="timeless")
            gender = gr.Dropdown(["feminine", "masculine", "androgynous", "fluid"], label="Gender Expression", value="fluid")
            audience = gr.Dropdown(["Gen Z trendsetters", "avant-garde collectors", "digital fashion enthusiasts"], label="Target Audience", value="digital fashion enthusiasts")
            garment = gr.Dropdown(["gown", "jacket", "bodysuit", "accessory"], label="Garment Type", value="gown")
            silhouette = gr.Dropdown(["structured", "flowing", "asymmetrical", "sculptural"], label="Silhouette Style", value="sculptural")
            color = gr.Dropdown(["muted earth tones", "neon brights", "monochrome", "iridescent"], label="Color Palette", value="iridescent")
            material = gr.Dropdown(["holographic silk", "liquid metal", "bio-textiles", "translucent mesh"], label="Material Concept", value="holographic silk")
            environment = gr.Dropdown(["virtual runway", "digital cathedral", "alien landscape"], label="Environment Context", value="virtual runway")
            influence = gr.Textbox(label="Cultural or Artistic Influence (optional)", value="Neo-Baroque Futurism")
            narrative = gr.Textbox(label="Narrative Element (optional)", value="A garment embodying transformation and digital transcendence.")
            guidance_scale = gr.Slider(label="Guidance Scale", minimum=1, maximum=20, value=7.5)
            generate_btn = gr.Button("Generate Fashion Design")
        with gr.Column():
            output = gr.Image(label="Generated Fashion Design")
    generate_btn.click(
        fn=generate_image,
        inputs=[mood, season, gender, audience, garment, silhouette, color, material, environment, influence, narrative, guidance_scale],
        outputs=output
    )

demo.launch()
