# rules.py

def rules_check(ucl, score, speed, amount):
    """
    Check the specified conditions and return the transaction status.
    
    Args:
        ucl (float): The UCL (Upper Control Limit) for the card.
        score (int): The credit score of the member.
        speed (float): The calculated speed of the transaction.
        amount (int): The amount of the current transaction.
    
    Returns:
        str: The status of the transaction, either 'FRAUD' or 'GENUINE'.
    """
    
    # If current transaction amount is greater than UCL, mark transaction as Fraud.
    if amount > ucl:
        return 'FRAUD'
    
    # If credit score is less than 250, reject as FRAUD.
    if score < 250:
        return 'FRAUD'
    
    # If speed is greater than 250, mark as FRAUD; else, mark as GENUINE.
    if speed > 250:
        return 'FRAUD'
    else:
        return 'GENUINE'
