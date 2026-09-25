# CrashZero — hosted demonstration

Predict Risk Before Impact.

This deployment contains the complete source tree, public data, and processed demo in `crashzero_source.zip`. Extract the archive to inspect the normal project structure. `streamlit_app.py` extracts it into an isolated runtime directory and launches the read-only cloud entrypoint. No remote executable code is fetched.

The hosted version provides historical analysis, maps, a conditional-injury model and preprocessed traffic video. Full video uploads and YOLO inference run locally using `./run.sh` from the extracted project after setup.

Source and media attribution, tests, model evaluation, and hackathon notes are included in the archive. NYC crash data is explicitly not Bengaluru history. Risk scores are unvalidated research indicators, not certified collision predictions.

Application code: AGPL-3.0-or-later. Public data and Pexels footage retain their respective terms.
