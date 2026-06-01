"""Entry point — run with `streamlit run main.py`."""
import runpy

if __name__ == "__main__":
    runpy.run_module("app.streamlit_app", run_name="__main__")
