#Опишите любую абстракцию (желательно юридическую,
# но вы можете выбрать любую другую) с помощью инструментов ООП (
# например, Истец-Ответчик, Право-Обязательство, Срок, Судья и др.).

#Придумайте атрибуты и методы для абстракции.
# Если ничего не приходит на ум, просто дополните абстракцию (класс)
# из домашнего задания № 7 любыми атрибутами и методами на ваше усмотрение.

class Contract:
    def __init__(self, contract_number: str, contract_type: str, parties: list, effective_date: str):
        self.contract_number = contract_number
        self.contract_type = contract_type
        self.parties = parties
        self.effective_date = effective_date
        self.terms = {}
        self.is_signed = False
        self.signing_date = None
        self.is_terminated = False
        self.termination_date = None

    def add_term(self, term_name: str, term_description: str) -> None:
        self.terms[term_name] = term_description

    def remove_term(self, term_name: str) -> None:
        if term_name in self.terms:
            del self.terms[term_name]

    def sign_contract(self, signing_date: str) -> None:
        self.is_signed = True
        self.signing_date = signing_date

    def add_party(self, party_name: str) -> None:
        self.parties.append(party_name)

    def remove_party(self, party_name: str) -> None:
        if party_name in self.parties:
            self.parties.remove(party_name)

    def terminate_contract(self, termination_date: str, reason: str) -> None:
        self.is_terminated = True
        self.termination_date = termination_date
        self.termination_reason = reason

    def get_contract_status(self) -> dict:
        return {
            "contract_number": self.contract_number,
            "is_signed": self.is_signed,
            "signing_date": self.signing_date,
            "is_terminated": self.is_terminated,
            "termination_date": self.termination_date if hasattr(self, 'termination_date') else None,
            "parties_count": len(self.parties),
            "terms_count": len(self.terms)
        }