# Delete Checklist Item

Delete a line item from a task checklist.

# OpenAPI definition

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "ClickUp API v2 Reference",
    "description": "The ClickUp API enables you to programmatically access and manage your ClickUp resources.\n\n## Authentication\nThe API supports two authentication methods:\n- **Personal API Token**: Use for testing and personal integrations. Add token to requests with header: `Authorization: pk_...`\n- **OAuth 2.0**: Required for building apps for other users. Uses authorization code flow.\n\n## Getting Started\nOur [Getting Started Guide](https://developer.clickup.com/docs/index) provides a comprehensive overview of how to use the ClickUp API.\n",
    "contact": {},
    "version": "2.0"
  },
  "jsonSchemaDialect": "https://json-schema.org/draft/2020-12/schema",
  "servers": [
    {
      "url": "https://api.clickup.com/api",
      "description": "ClickUp",
      "variables": {}
    }
  ],
  "paths": {
    "/v2/checklist/{checklist_id}/checklist_item/{checklist_item_id}": {
      "delete": {
        "summary": "Delete Checklist Item",
        "tags": [
          "Task Checklists"
        ],
        "description": "Delete a line item from a task checklist.",
        "operationId": "DeleteChecklistItem",
        "parameters": [
          {
            "name": "checklist_id",
            "in": "path",
            "description": "b8a8-48d8-a0c6-b4200788a683 (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "b955c4dc"
              ]
            }
          },
          {
            "name": "checklist_item_id",
            "in": "path",
            "description": "e491-47f5-9fd8-d1dc4cedcc6f (uuid)",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "21e08dc8"
              ]
            }
          }
        ],
        "responses": {
          "200": {
            "description": "",
            "headers": {},
            "content": {
              "application/json": {
                "schema": {
                  "type": "object",
                  "examples": [
                    {}
                  ],
                  "contentMediaType": "application/json"
                },
                "example": {}
              }
            }
          }
        },
        "deprecated": false
      },
      "parameters": []
    }
  },
  "components": {
    "securitySchemes": {
      "Authorization_Token": {
        "name": "Authorization",
        "type": "apiKey",
        "in": "header",
        "description": "API token required for authentication. Two types of tokens are supported:\n**Personal API Key** Obtain from ClickUp's settings page under 'Apps' and add it to the header as `Authorization: pk_...`\n**OAuth2 Access Token** Generated through the OAuth2 flow and add it to the header as `Authorization: Bearer {access_token}`"
      }
    }
  },
  "security": [
    {
      "Authorization_Token": []
    }
  ],
  "tags": [
    {
      "name": "Task Checklists"
    }
  ]
}
```