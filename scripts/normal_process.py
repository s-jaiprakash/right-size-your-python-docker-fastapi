def clean_quantity(df):
    df['cleaned_quantity'] = df["quantity"]
    df['cleaned_quantity'] = (
        df['cleaned_quantity']
        .astype(str)
        .str.replace(r"[^\d-]", "", regex=True)  # Remove everything except digits and minus sign
        .replace("", "0")                        # Replace empty strings with "0"
        .astype(int)
    )
    return df
