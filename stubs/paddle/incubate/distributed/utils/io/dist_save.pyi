from .save_for_auto import save_for_auto_inference as save_for_auto_inference

__all__ = ['save', 'save_for_auto_inference']

def save(state_dict, path, **configs): ...
