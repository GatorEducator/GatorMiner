#!/usr/bin/env python3

import pandas as pd
import numpy as np
import altair as alt

df = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])

c = alt.Chart(df).mark_circle().encode(x="a", y="b", size="c", color="c")

st.vega_lite_chart(
    df,
    {
        "mark": "circle",
        "encoding": {
            "x": {"field": "a", "type": "quantitative"},
            "y": {"field": "b", "type": "quantitative"},
            "size": {"field": "c", "type": "quantitative"},
            "color": {"field": "c", "type": "quantitative"},
        },
    },
)
