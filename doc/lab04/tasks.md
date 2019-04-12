# Typy zadań

- obsługa metod specjalnych
- obsługa obiektu jako słownika
- wykorzystanie sztucznych obiektów

# Asercje

```
assertTrue
assertFalse
assertEqual
assertNotEqual
assertIn
assertNotIn
```

# Zadania

Dokończ test `test_context`, który sprawdza, czy obiekt testowy `self.task` posiada poprawnie ustawiony kontekst, porównując `self.context` z `self.task.context` w przypadku testowym `test_context`, wykorzystując asercję `self.assertEqual`.

Dokończ test `test_function`, który sprawdza, czy obiekt testowy `self.task` posiada poprawnie ustawioną funkcję, porównując `self.function` z `self.task.function` w przypadku testowym `test_function`, , wykorzystując asercję `self.assertEqual`.

---

Dokończ test `test_another_task_with_same_context_and_function`, który sprawdza, czy obiekt testowy `self.task` jest podobny do innego (nowego) obiektu `another_task`, jeśli ma ten sam kontekts `self.context` i tę samą funkcję `self.function`, wykorzystując asercję `self.assertEqual`.

Dokończ test `test_another_task_with_different_function_but_same_context`, który sprawdza, czy obiekt testowy `self.task` jest niepodobny do innego (nowego) obiektu `another_task`, jeśli ma ten sam kontekts `self.context`, ale ma inną (nową) funkcję `another_function`, wykorzystując asercję `self.assertNotEqual`.

Dokończ test `test_another_task_with_different_context_but_same_function`, który sprawdza, czy obiekt testowy `self.task` jest niepodobny do innego (nowego) obiektu `another_task`, jeśli ma tę samą funkcję `self.function`, ale ma inny (nowy) kontekts `another_context`, wykorzystując asercję `self.assertNotEqual`.

Dokończ test `test_another_task_with_different_context_and_function`, który sprawdza, czy obiekt testowy `self.task` jest niepodobny do innego (nowego) obiektu `another_task`, jeśli ma ma inny (nowy) kontekts `another_context` i ma inną (nową) funkcję `another_function`, wykorzystując asercję `self.assertNotEqual`.

---

Dokończ test `test_get_named_argument`, który sprawdza, czy ustawione przy tworzeniu obiektu `self.task` nazwane argumenty `named_arguments` są poprawnie odczytywane, wykorzystując konstrukcję `self.task[self.key]` i porównując wynik do oczekiwanej wartości `self.value`, jaka została przypisana przy tworzeniu obiektu `self.test` w `setUp`, wykorzystując asercję `self.assertEqual`.

Dokończ test `test_contains_named_argument`, który sprawdza, czy ustawione przy tworzeniu obiektu `self.task` nazwane argumenty `named_arguments` są poprawnie sprawdzane "czy istnieją", wykorzystując konstrukcję `self.key in self.task` z asercją `self.assertTrue` lub wykorzystując odpowiednią asercję `self.assertIn`. Można obie konstrukcje umieścić w teście.

Dokończ test `test_update_named_argument`, który sprawdza, czy ustawione przy tworzeniu obiektu `self.task` nazwane argumenty `named_arguments` można nadpisać, wykorzystując konstrukcję `self.task[self.key] = another_value` i odczytać, wykorzystując konstrukcje `self.task[self.key]` i porównując wynik do oczekiwanej wartości `another_value`, wykorzystując asercję `self.assertEqual`.

Dokończ test `test_delete_named_argument`, który sprawdza, czy usuwa się nazwany argument `self.key`, ustawiony przy tworzeniu obiektu `self.task`, wykorzystując konstrukcję `del self.task[self.key]` i czy nie istnieje (po usunięciu), wykorzystując konstrukcję `self.key not in self.task` z asercją `self.assertTrue` lub konstrukcję `self.key in self.task` z asercją `self.assertFalse` lub wykorzystując odpowiednią asercję `self.assertNotIn`.

---

Dokończ test `test_set_and_get_named_argument`, który sprawdza, czy można poprawnie odczytać wartości zapisane przy użyciu konstrukcji `self.task[key] = value`, poprzez konstrukcję `self.task[key]` i porównując wynik do oczekiwanej wartości `value`, wykorzystując asercję `self.assertEqual`.

Dokończ test `test_set_and_check_named_argument`, który sprawdza, czy można poprawnie sprawdzić, czy istnieją wartości zapisane przy użyciu konstrukcji `self.task[key] = value`, poprzez konstrukcję `key in self.task` z asercją `self.assertTrue` lub wykorzystując odpowiednią asercję `self.assertIn`.

Dokończ test `test_set_and_delete_named_argument`, który sprawdza, czy można poprawnie usunąć wartości, zapisane przy użyciu konstrukcji `self.task[key] = value`, wykonując `del self.task[key]` i sprawdzając, czy nie istnieje, wykorzystując konstrukcję `key not in self.task` z asercją `self.assertTrue` lub konstrukcję `key in self.task` z asercją `self.assertFalse` lub wykorzystując odpowiednią asercję `self.assertNotIn`.

---

Dokończ test `test_name`, który sprawdza, czy ustawiona przy tworzeniu nazwa `self.name`, jest poprawnie formatowana przy odczytywaniu `self.task.name`, wykorzystując assercję `self.assertEqual`.

Dokończ test `test_change_name`, który sprawdza, czy zmiana nazwy na `new_name`, poprawnie jest używana przy odczytywaniu `self.task.name`, wykorzystując assercję `self.assertEqual`.

Dokończ test `test_description`, który sprawdza, czy domyślnie ustawiony opis, jest poprawnie formatowany przy odczytywaniu `self.task.description`, wykorzystując assercję `self.assertEqual`.

Dokończ test `test_change_description`, który sprawdza, czy zmiana opisu na `new_description`, poprawnie jest używane przy odczytywaniu `self.task.description`, wykorzystując assercję `self.assertEqual`.

---

Dokończ test `test_str`, który sprawdza, czy wynik formatowania dla funkcji wbudowanej `str()`, zwraca poprawny wynik dla obiektu `self.task`, wykorzystując asercję `self.assertEqual`.

