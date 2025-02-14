"""
Created on 2024-02-14

@author: wf
"""
from nicegui import ui
from dataclasses import dataclass
from typing import Optional

@dataclass
class ContentGenerator:
    """
    Generator for learning content
    """
    def __init__(self, llm):
        """
        Initialize me with the given llm

        Args:
            llm: the Large Language Model to use
        """
        self.llm = llm

    def get_prompt(self, content: str, profile: str) -> str:
        """
        create a prompt for the given content and profile

        Args:
            content(str): the learning content
            profile(str): the learner profile

        Returns:
            str: the prompt
        """
        prompt = f"""Given this learning element:
{content}

And this learner profile:
{profile}

Generate flashcard style learning content with:
- Key Concepts
- Examples relevant to the profile's interests
- Practice Questions
- Related Topics

Format as markdown."""
        return prompt

    def generate(self, content: str, profile: str) -> Optional[str]:
        """
        generate content based on the given input

        Args:
            content(str): the learning content
            profile(str): the learner profile

        Returns:
            str: the generated content or None on error
        """
        try:
            prompt = self.get_prompt(content, profile)
            result = self.llm.ask(prompt)
            return result
        except Exception as ex:
            # Pass the error up to be handled by the view
            raise ex

class LearningView:
    """
    View for learning content generation using LLM
    """

    def __init__(self, solution):
        """
        Initialize with the given solution as backpointer

        Args:
            solution: the solution context this view belongs to
        """
        self.solution = solution
        self.content_generator = ContentGenerator(self.solution.llm)

    def create_textarea(
        self, label: str, placeholder: Optional[str] = None, height: str = "h-32"
    ) -> ui.textarea:
        """Create a consistent textarea with error handling"""
        return (
            ui.textarea(label=label, placeholder=placeholder)
            .classes(f"w-full {height}")
            .props("clearable outlined")
        )

    def setup(self):
        """
        Setup the UI components for the learning content view
        """
        try:
            with self.solution.content_div:
                with ui.splitter() as splitter:
                    with splitter.before:
                        with ui.row().classes('w-full') as self.input_row:
                            ui.label('What would you like to learn?').classes('text-xl font-bold')
                            with ui.grid(columns=1).classes('gap-4'):
                                self.element_input = self.create_textarea(
                                    label='Learning Element',
                                    placeholder='Enter Slide/Quiz/Goal/Chapter...'
                                ).classes('w-full')

                                self.profile_input = self.create_textarea(
                                    label='Learner Profile',
                                    placeholder='Enter your background...'
                                ).classes('w-full')

                                ui.button('Generate Learning Content', on_click=self.generate).classes('w-full')

                    with splitter.after:
                        self.result_display = ui.markdown().classes('w-full')
        except Exception as ex:
            self.solution.handle_exception(ex)

    async def generate(self):
        """
        Generate learning content using LLM
        """
        try:
            if not self.element_input.value or not self.profile_input.value:
                ui.notify('Please fill in both fields')
                return

            result = self.content_generator.generate(
                self.element_input.value,
                self.profile_input.value
            )
            self.result_display.content = result

        except Exception as ex:
            ui.notify(f'Error: {str(ex)}')
            if hasattr(self.solution, 'logger'):
                self.solution.logger.error(f'Content generation failed: {str(ex)}')