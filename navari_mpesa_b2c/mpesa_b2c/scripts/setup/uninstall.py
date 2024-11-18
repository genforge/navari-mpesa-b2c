import click
import frappe

from ....hooks import app_email, fixtures


def delete_custom_fields():
    """Delete custom fields"""
    click.secho("Removing customisations", fg="green")

    try:
        frappe.db.delete(
            doctype=fixtures[0]["doctype"],
            filters=fixtures[0]["filters"],
        )

    except Exception as e:
        click.secho(
            (
                "Removal of customisations failed due to an error.",
                "Please try again.",
                f"If error persists, please report to following email: {app_email}",
            ),
            fg="bright_red",
        )
        raise e
