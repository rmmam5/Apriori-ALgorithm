import pandas as pd
import streamlit as st
from src.data_loader import read_transactions
from src.apriori import apriori
from src.generate_rules import generate_association_rules
from src.visualization import plot_frequent_itemsets


st.set_page_config(
    page_title="Apriori Algorithm Analysis",
    page_icon="📊",
    layout="wide",
)

st.title("Apriori Algorithm")
st.write(
    "Upload an Excel transaction file, set Minimum Support and Minimum Confidence, then run Apriori to view frequent itemsets and association rules."
)

with st.sidebar:
    st.header("Input settings")
    uploaded_file = st.file_uploader(
        "Choose an Excel file",
        type=["xlsx", "xls"],
    )

    min_support = st.number_input(
        "Minimum Support",
        min_value=0.01,
        max_value=1.00,
        value=0.60,
        step=0.01,
    )

    min_confidence = st.number_input(
        "Minimum Confidence",
        min_value=0.01,
        max_value=1.00,
        value=0.80,
        step=0.01,
    )

    run_button = st.button(
        "Run Apriori",
        type="primary",
        use_container_width=True,
        disabled=uploaded_file is None,
    )

if uploaded_file is None:
    st.info("Upload an Excel file from the sidebar to begin.")
    st.stop()

preview_df = pd.read_excel(uploaded_file, dtype=str)
st.subheader("Excel preview")
st.dataframe(preview_df, use_container_width=True)

if run_button:
    try:
        transactions = read_transactions(uploaded_file)
        if not transactions:
            st.warning(
                "No Transactions were found"
            )
            st.stop()

        with st.spinner("Running Apriori and Generating Association Rules..."):
            levels, supports = apriori(transactions, min_support)
            plot_frequent_itemsets(supports)
            rules = generate_association_rules(
                levels,
                supports,
                min_confidence,
            )

        frequent_rows = []
        for level_number, itemsets in levels.items():
            for itemset in itemsets:
                frequent_rows.append(
                    {
                        "Itemset": ", ".join(sorted(str(item) for item in itemset)),
                        "Items Count": len(itemset),
                        "Support": supports[itemset],
                        "Level": level_number,
                    }
                )

        frequent_df = pd.DataFrame(
            frequent_rows,
            columns=["Itemset", "Items Count", "Support", "Level"],
        )
        if not frequent_df.empty:
            frequent_df = frequent_df.sort_values(
                by=["Items Count", "Support"],
                ascending=[True, False],
            ).reset_index(drop=True)
        rule_rows = []
        for rule in rules:
            rule_rows.append(
                {
                    "Antecedent": ", ".join(sorted(rule["Antecedent"])),
                    "Consequent": ", ".join(sorted(rule["Consequent"])),
                    "Support": rule["Support"],
                    "Confidence": rule["Confidence"],
                    "Lift": rule["Lift"],
                    "The Association": rule["The Association"],
                }
            )

        rules_df = pd.DataFrame(
            rule_rows,
            columns=[
                "Antecedent",
                "Consequent",
                "Support",
                "Confidence",
                "Lift",
                "The Association",
            ],
        )

        st.success(f"Analyzed {len(transactions)} transactions.")

        metric1, metric2, metric3 = st.columns(3)
        metric1.metric("Transactions", len(transactions))
        metric2.metric("Frequent itemsets", len(frequent_df))
        metric3.metric("Association rules", len(rules_df))

        tab_itemsets, tab_rules, tab_visualization = st.tabs(
            ["Frequent Itemsets", "Association Rules", "Visualization"]
        )

        with tab_itemsets:
            st.subheader("Frequent Itemsets")
            if frequent_df.empty:
                st.warning("No frequent itemsets matched the Minimum Support.")
            else:
                st.dataframe(frequent_df, use_container_width=True)
                st.download_button(
                    "Export Frequent Itemsets as CSV",
                    data=frequent_df.to_csv(index=False).encode("utf-8-sig"),
                    file_name="frequent_itemsets.csv",
                    mime="text/csv",
                )

        with tab_rules:
            st.subheader("Association Rules")
            if rules_df.empty:
                st.warning(
                    "No association rules matched the Minimum Confidence."
                )
            else:
                st.dataframe(rules_df, use_container_width=True)
                st.download_button(
                    "Export Association rules as CSV",
                    data=rules_df.to_csv(index=False).encode("utf-8-sig"),
                    file_name="association_rules.csv",
                    mime="text/csv",
                )

        with tab_visualization:
            st.subheader("Frequent Itemsets Support Chart")
            if frequent_df.empty:
                st.info("There are no frequent itemsets to visualize.")
            else:
                chart_df = frequent_df.set_index("Itemset")[["Support"]]
                st.bar_chart(chart_df)


    except Exception as exc:
        st.error(f"Could not run the analysis: {exc}")
        st.exception(exc)



