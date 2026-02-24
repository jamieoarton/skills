# Get View

View information about a specific task or page view. The information returned about a view varies by the type of view.

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
    "/v2/view/{view_id}": {
      "get": {
        "summary": "Get View",
        "tags": [
          "Views"
        ],
        "description": "View information about a specific task or page view. The information returned about a view varies by the type of view.",
        "operationId": "GetView",
        "parameters": [
          {
            "name": "view_id",
            "in": "path",
            "description": "",
            "required": true,
            "style": "simple",
            "schema": {
              "type": "string",
              "examples": [
                "3c-105"
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
                  "title": "GetViewresponse",
                  "oneOf": [
                    {
                      "title": "List View",
                      "type": "object",
                      "properties": {
                        "view": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "type": {
                              "type": "string",
                              "enum": [
                                "list"
                              ]
                            },
                            "parent": {
                              "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/parent"
                            },
                            "grouping": {
                              "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/grouping"
                            },
                            "divide": {
                              "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/divide"
                            },
                            "sorting": {
                              "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/sorting"
                            },
                            "filters": {
                              "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/filters"
                            }
                          },
                          "columns": {
                            "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/columns"
                          },
                          "team_sidebar": {
                            "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/team_sidebar"
                          },
                          "settings": {
                            "$ref": "#/paths/~1v2~1view~1%7Bview_id%7D/put/requestBody/content/application~1json/schema/properties/settings"
                          }
                        }
                      },
                      "examples": [
                        {
                          "view": null,
                          "id": "3c-105",
                          "name": "New Team View Name",
                          "type": "list",
                          "parent": {
                            "id": "512",
                            "type": 7
                          },
                          "grouping": {
                            "field": "status",
                            "dir": 1,
                            "collapsed": [],
                            "ignore": false
                          },
                          "divide": {
                            "field": null,
                            "dir": null,
                            "collapsed": []
                          },
                          "sorting": {
                            "fields": {
                              "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                              "dir": -1,
                              "idx": 0
                            }
                          },
                          "filters": {
                            "op": "AND",
                            "fields": [],
                            "search": "",
                            "show_closed": false
                          },
                          "columns": {
                            "fields": []
                          },
                          "team_sidebar": {
                            "assignees": [],
                            "assigned_comments": false,
                            "unassigned_tasks": false
                          },
                          "settings": {
                            "show_task_locations": false,
                            "show_subtasks": 3,
                            "show_subtask_parent_names": false,
                            "show_closed_subtasks": false,
                            "show_assignees": true,
                            "show_images": true,
                            "collapse_empty_columns": null,
                            "me_comments": true,
                            "me_subtasks": true,
                            "me_checklists": true
                          }
                        }
                      ]
                    },
                    {
                      "title": "Form View",
                      "type": "object",
                      "properties": {
                        "view": {
                          "type": "object",
                          "properties": {
                            "id": {
                              "type": "string"
                            },
                            "name": {
                              "type": "string"
                            },
                            "type": {
                              "type": "string",
                              "enum": [
                                "form"
                              ]
                            },
                            "parent": {
                              "type": "object",
                              "properties": {
                                "id": {
                                  "type": "string"
                                },
                                "type": {
                                  "type": "integer"
                                }
                              },
                              "additionalProperties": false
                            },
                            "date_created": {
                              "type": "string"
                            },
                            "creator": {
                              "type": "integer"
                            },
                            "visibility": {
                              "type": "string"
                            },
                            "protected": {
                              "type": "boolean"
                            },
                            "protected_note": {
                              "type": "null"
                            },
                            "protected_by": {
                              "type": "null"
                            },
                            "date_protected": {
                              "type": "null"
                            },
                            "orderindex": {
                              "type": "integer"
                            },
                            "public": {
                              "type": "boolean"
                            },
                            "public_url": {
                              "type": "string",
                              "format": "url"
                            }
                          }
                        }
                      },
                      "examples": [
                        {
                          "view": null,
                          "id": "6kgye-11235",
                          "name": "Project Intake Form",
                          "type": "form",
                          "parent": {
                            "id": 900902118235,
                            "type": 6
                          },
                          "date_created": 1762302043575,
                          "creator": 1234,
                          "visibility": "public",
                          "protected": false,
                          "protected_note": null,
                          "protected_by": null,
                          "date_protected": null,
                          "orderindex": 9,
                          "public": true,
                          "public_url": "https://forms.clickup.com/1234/f/6kgye-11896/KA64ABC123"
                        }
                      ]
                    }
                  ]
                },
                "example": [
                  {
                    "view": {
                      "id": "3c-105",
                      "name": "New View Name",
                      "type": "list",
                      "parent": {
                        "id": "512",
                        "type": 7
                      },
                      "grouping": {
                        "field": "status",
                        "dir": 1,
                        "collapsed": [],
                        "ignore": false
                      },
                      "divide": {
                        "field": null,
                        "dir": null,
                        "collapsed": []
                      },
                      "sorting": {
                        "fields": [
                          {
                            "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                            "dir": -1,
                            "idx": 0
                          }
                        ]
                      },
                      "filters": {
                        "op": "AND",
                        "fields": [
                          {
                            "field": "cf_624a423a-c1d1-4467-99e2-63e225658cb2",
                            "op": "EQ",
                            "determinor": null,
                            "idx": 0,
                            "values": "123"
                          }
                        ],
                        "search": "",
                        "show_closed": false
                      },
                      "columns": {
                        "fields": [
                          {
                            "field": "assignee",
                            "idx": 0,
                            "width": 160,
                            "hidden": true,
                            "name": null,
                            "display": null
                          }
                        ]
                      },
                      "team_sidebar": {
                        "assignees": [],
                        "assigned_comments": false,
                        "unassigned_tasks": false
                      },
                      "settings": {
                        "show_task_locations": false,
                        "show_subtasks": 3,
                        "show_subtask_parent_names": false,
                        "show_closed_subtasks": false,
                        "show_assignees": true,
                        "show_images": true,
                        "collapse_empty_columns": null,
                        "me_comments": true,
                        "me_subtasks": true,
                        "me_checklists": true
                      }
                    }
                  },
                  {
                    "view": null,
                    "id": "6kgye-11234",
                    "name": "Project Intake Form",
                    "type": "form",
                    "parent": {
                      "id": 900902118235,
                      "type": 6
                    },
                    "date_created": 1762302043575,
                    "creator": 1234,
                    "visibility": "public",
                    "protected": false,
                    "protected_note": null,
                    "protected_by": null,
                    "date_protected": null,
                    "orderindex": 9,
                    "public": true,
                    "public_url": "https://forms.clickup.com/1234/f/6kgye-11896/KA64ABC123"
                  }
                ]
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
      "name": "Views"
    }
  ]
}
```