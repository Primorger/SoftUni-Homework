class IDMixin:
    id: int = 1

    @classmethod
    def get_next_id(cls) -> int:
        return cls.id
    
    @classmethod
    def increment_id(cls) -> int:
        cls.id += 1