import argparse
import logging
import sys
import os 
from PIL import Image
from pygame_renderer import PyGameTextRenderer
logger = logging.getLogger(__name__)

renderer_name_or_path = "noto_renderer"


def process_doc(
    doc: str, #str or list[str] or tuple(str, str)
):
    text_renderer = PyGameTextRenderer.from_pretrained(renderer_name_or_path)
    max_pixels = text_renderer.pixels_per_patch * text_renderer.max_seq_length - 2 * text_renderer.pixels_per_patch
    target_seq_length = max_pixels
    data = {"pixel_values": [], "num_patches": [], 'text': []}

    doc = doc.strip().split("\n")
    # doc = [doc.strip()]
    width = 0
    block = []
    
    for line in doc:
        
        line_width = text_renderer.font.get_rect(line).width
        if width + line_width >= target_seq_length:
            

            sequence = " ".join(block)
            
            encoding = text_renderer(text=sequence)
            
            data["pixel_values"].append(Image.fromarray(encoding.pixel_values))
            # data["pixel_values"].append(encoding.pixel_values)
        
            data["num_patches"].append(encoding.num_text_patches)
            data["text"].append(sequence)  

            width = line_width
            block = [line]
        else:
            block.append(line)
            width += line_width
    if len(block) > 0:
        sequence = " ".join(block)
        encoding = text_renderer(text=sequence)

        data["pixel_values"].append(Image.fromarray(encoding.pixel_values))
        data["num_patches"].append(encoding.num_text_patches)
        data["text"].append(sequence)


    return data
